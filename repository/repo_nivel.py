from bson.objectid import ObjectId
from config.connection import Connection

class NivelRepo:

    def __init__(self):
        self.conn = Connection('test')
        self.collection = 'niveles'

    def all_niveles(self):
        try:
            records = self.conn.get_all(self.collection)
            
            for record in records:
                print(f'ID: {record["_id"]}')
                print(f'Nivel: {record["nivel"]}')
                print(f'Estado: {record["estado"]}')
                print('=====================')
        except Exception as e:
            print(e)


    def one_nivel(self,id):
        try:    
            condition = {
                '_id' : ObjectId(id)
            }
            records = self.conn.get_one(self.collection, condition)

            print(f'ID: {records["_id"]}')
            print(f'Nivel: {records["nivel"]}')
            print(f'Estado: {records["estado"]}')
            print('=====================')
            return records
        except Exception as ex:
            print(ex)
    
    def insert_nivel(self, data):
        try:  
            self.conn.insert(self.collection, data)
            print(f'se registro correctamente el nivel')
        except Exception as ex:
            print(ex)

    def update_nivel(self, id_object, data):
        try:
            id_object = {
                '_id' : ObjectId(id_object)
            }
            self.conn.update(self.collection, id_object, data)
            print(f'Se actualizó correctamente al nivel')
            return True
        except Exception as ex:
            print(str(ex))

    def inhabilitar_nivel(self, id_object):
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

    def niveles_habilitados(self):
        try:
            condition = {
                'estado' : 'true'
            }
            records = self.conn.get_all_by(self.collection, condition)
            for record in records:
                    print(f'ID: {record["_id"]}')
                    print(f'Nivel: {record["nivel"]}')
                    print(f'Estado: {record["estado"]}')
                    print('=====================')
        except Exception as ex:
            print(str(ex))