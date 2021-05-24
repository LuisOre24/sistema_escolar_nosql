from threading import Condition
from bson.objectid import ObjectId
from config.connection import Connection

class CursoRepo:

    def __init__(self):
        self.conn = Connection('test')
        self.collection = 'cursos'

    def all_cursos(self):
        try:
            records = self.conn.get_all(self.collection)
            for record in records:
                print(f'ID: {record["_id"]}')
                print(f'Curso: {record["descripcion"]}')
                print(f'Categoria: {record["categoria"]}')
                print(f'Estado: {record["estado"]}')
                print('=====================')
        except Exception as e:
            print(e)
    
    def one_curso(self,id):
        try: 
            id = {
                '_id' : ObjectId(id)
            }   
            records = self.conn.get_one(self.collection, id)
            print(f'ID: {records["_id"]}')
            print(f'Curso: {records["descripcion"]}')
            print(f'Categoria: {records["categoria"]}')
            print(f'Estado: {records["estado"]}')
            print('=====================')
            return records
        except Exception as ex:
            print(ex)
    
    def insert_curso(self, data):
        
        try:  
            self.conn.insert(self.collection, data)
            print(f'se registro correctamente el curso')
        except Exception as ex:
            print(ex)

    def update_curso(self, id_object, data):
        try:  
            id_object = {
                '_id' : ObjectId(id_object)
            }
            self.conn.update(self.collection, data)
            print(f'se actualizo correctamente el curso')
        except Exception as ex:
            print(ex)
        return True

    def inhabilitar_curso(self, id_object):
        try:  
            id_object = {
                '_id' : ObjectId(id_object)
            }
            data = {
                'estado' : 'false'
            }
            self.conn.update(self.collection, data)
            print(f'se deshabilito correctamente el curso')
        except Exception as ex:
            print(ex)
        return True

    def cursos_habilitados(self):
        try:  
            condition = {
                'estado' : 'true'
            }
            records = self.conn.get_all_by(condition)

            for record in records:
                    print(f'ID: {record["_id"]}')
                    print(f'Curso: {record["descripcion"]}')
                    print(f'Categoria: {record["categoria"]}')
                    print(f'Estado: {record["estado"]}')
                    print('=====================')
        except Exception as ex:
            print(ex)