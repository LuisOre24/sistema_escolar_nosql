from bson.objectid import ObjectId
from config.connection import Connection

class CategoriaRepo:

    def __init__(self):
        self.conn = Connection('test')
        self.collection = 'categorias'
           
    def all_categorias(self):
        try:
            records = self.conn.get_all(self.collection)
            for record in records:
                print(f'ID: {record["_id"]}')
                print(f'Descipcion: {record["descripcion"]}')
                print(f'Estado: {record["estado"]}')
                print('=====================')
        except Exception as e:
            print(e)
    
    def one_categoria(self,id):
        try:    
            id = {
                '_id' : ObjectId(id)
            }
            records = self.conn.get_one(id)
            print(f'ID: {records["_id"]}')
            print(f'Descripcion: {records["descripcion"]}')
            print(f'Estado: {records["estado"]}')
            print('=====================')
            return records
        except Exception as ex:
            print(ex)
    
    def insert_categoria(self, data):
        try:  
            self.conn.insert(self.collection, data)
            print(f'se registro correctamente la categoria')
        except Exception as ex:
            print(ex)

    def update_categoria(self, id_object, data):
        try:
            id_object = {
            '_id' : ObjectId(id_object)
            }
            self.conn.update(self.collection, id_object, data)
        except Exception as ex:
            print(f'error al actualizar categoria. Error Code: {str(ex)}')  
        return True

    def inhabilitar_categoria(self,parameter, id_object):
        try:
            id_object = {
            '_id' : ObjectId(id_object)
            }
            data = {
                'estado' : 'false'
            }
            self.conn.update(self.collection, id_object, data)
        except Exception as ex:
            print(f'error al actualizar categoria. Error Code: {str(ex)}') 
        return True

    def categorias_habilitados(self):
        try:
            condition = {
                'estado' :  'true'
            }
            records = self.conn.get_all_by(self.collection,condition)
            for record in records:
                print(f'ID: {record["_id"]}')
                print(f'Descripcion: {record["descripion"]}')
                print(f'Estado: {record["estado"]}')
                print('=====================')
        except Exception as ex:
            print(str(ex))