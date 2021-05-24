from bson.objectid import ObjectId
from config.connection import Connection

class PeriodoRepo:

    def __init__(self):
        self.conn = Connection('test')
        self.collection = 'periodos'

    def all_periodos(self):
        try:
            records = self.conn.get_all(self.collection)
            for record in records:
                print(f'ID: {record["_id"]}')
                print(f'Mes: {record["mes"]}')
                print(f'Año: {record["anio"]}')
                print(f'Estado: {record["estado"]}')
                print('=====================')
        except Exception as e:
            print(e)
    
    def one_periodo(self,id):
        try:    
            condition  = {
                '_id' : ObjectId(id)
            }
            records = self.conn.get_one(self.collection, condition)
            print(f'ID: {records["_id"]}')
            print(f'Mes: {records["mes"]}')
            print(f'Año: {records["anio"]}')
            print(f'Estado: {records["estado"]}')
            print('=====================')
            return records
        except Exception as ex:
            print(ex)
    
    def insert_periodo(self, data):
        
        try:  
            self.conn.insert(self.collection, data)
            print(f'se registro correctamente el periodo')
        except Exception as ex:
            print(ex)

    def update_periodo(self, id_object, data):
        try:
            id_object = {
                '_id' : ObjectId(id_object)
            }
            self.conn.update(self.collection, id_object, data)
            print("Se actulizo el periodo correctamente")
        except Exception as ex:
            print(str(ex))
    
    def inhabilitar_periodo(self, id_object):
        try:
            id_object = {
                '_id' : ObjectId(id_object)
            }
            data = {
                'estado' : 'false'
            }
            self.conn.update(self.collection, id_object, data)
            print("Se inhabilito correctamente el periodo")
            return True
        except Exception as ex:
            print(str(ex))

    def periodos_habilitados(self):
        try:
            condition = {
                'estado' : 'true'
            }
            records = self.conn.get_all_by(self.collection, condition)
            for record in records:
                    print(f'ID: {record["_id"]}')
                    print(f'Mes: {record["mes"]}')
                    print(f'Año: {record["anio"]}')
                    print(f'Estado: {record["estado"]}')
                    print('=====================')
        except Exception as ex:
            print(str(ex))