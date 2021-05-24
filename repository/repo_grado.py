from threading import Condition

from bson.objectid import ObjectId
from config.connection import Connection

class GradoRepo:

    def __init__(self):
        self.conn = Connection('test')
        self.collection = 'grados'            

    def all_grados(self):
        try:
            records = self.conn.get_all(self.collection)
            for record in records:
                print(f'ID: {record["_id"]}')
                print(f'Grado: {record["grado"]}')
                print(f'Nivel: {record["nivel"]}')
                print(f'Estado: {record["estado"]}')
                print('=====================')
        except Exception as e:
            print(e)
    
    def one_grado(self,id):
        try:    
            condition = {
                '_id' : ObjectId(id)
            }
            records = self.conn.get_one(self.collection, condition)

            print(f'ID: {records["_id"]}')
            print(f'Grado: {records["grado"]}')
            print(f'Nivel: {records["nivel"]}')
            print(f'Estado: {records["estado"]}')
            print('=====================')
            return records
        except Exception as ex:
            print(ex)
    
    def insert_grado(self, data):
        try:  
            self.conn.insert(self.collection, data)
            print(f'se registro correctamente el grado')

        except Exception as ex:
            print(ex)

    def update_grado(self, id_object, data):
        try:
            id_object = {
                '_id' : ObjectId(id_object)
            }
            self.conn.update(self.collection, id_object, data)
            print(f'Se actualizó correctamente al grado')
            return True
        except Exception as ex:
            print(str(ex))

    def inhabilitar_grado(self, id_object):
        try:
            id_object = {
                '_id' : ObjectId(id_object)
            }
            data = {
                'estado' : 'false'
            }
            self.conn.update(self.collection, id_object, data)
        except Exception as ex:
            print(f'Error : {str(ex)}')
        return True

    def grados_habilitados(self):
        try:
            condition = {
                'estado' : 'true'
            }
            records = self.conn.get_all_by(self.collection, condition)
            for record in records:
                    print(f'ID: {record["_id"]}')
                    print(f'Grado: {record["grado"]}')
                    print(f'Nivel: {record["nivel"]}')
                    print(f'Estado: {record["estado"]}')
                    print('=====================')
        except Exception as ex:
            print(str(ex))

