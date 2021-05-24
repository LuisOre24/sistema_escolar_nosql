from bson.objectid import ObjectId
from config.connection import Connection

class SeccionRepo:

    def __init__(self):
        self.conn = Connection('test')
        self.collection = 'secciones'

    def all_secciones(self):
        try:
            records = self.conn.get_all(self.collection)
            
            for record in records:
                print(f'ID: {record["_id"]}')
                print(f'Seccion: {record["seccion"]}')
                print(f'Estado: {record["estado"]}')
                print('=====================')
        except Exception as e:
            print(e)


    def one_seccion(self,id):
        try:    
            condition = {
                '_id' : id
            }
            records = self.conn.get_one(self.collection, condition)

            print(f'ID: {records["_id"]}')
            print(f'Seccion: {records["seccion"]}')
            print(f'Estado: {records["estado"]}')
            print('=====================')
            return records
        except Exception as ex:
            print(ex)
    
    def insert_seccion(self, data):
        try:  
            self.conn.insert(self.collection, data)
            print(f'se registro correctamente el seccion')

        except Exception as ex:
            print(ex)

    def update_seccion(self, id_object, data):
        try:
            id_object = {
                '_id' : ObjectId(id_object)
            }
            self.conn.update(self.collection, id_object, data)
            print(f'Se actualizó correctamente al seccion')
            return True
        except Exception as ex:
            print(str(ex))

    def inhabilitar_seccion(self, id_object):
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

    def secciones_habilitados(self):
        try:
            condition = {
                'estado' : 'true'
            }
            records = self.conn.get_all_by(self.collection, condition)
            for record in records:
                    print(f'ID: {record["_id"]}')
                    print(f'Seccion: {record["seccion"]}')
                    print(f'Estado: {record["estado"]}')
                    print('=====================')
        except Exception as ex:
            print(str(ex))