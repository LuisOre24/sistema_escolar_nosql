from bson.objectid import ObjectId
from pymongo import collection
from config.connection import Connection

class AlumnoRepo:

    def __init__(self):
        self.conn = Connection('test')
        self.collection = 'alumnos'

    def all_alumnos(self):
        try:
            records = self.conn.get_all(self.collection)
            #print(records)
            for record in records:
                print(f'ID: {record["_id"]}')
                print(f'Nombres: {record["nombres"]}')
                print(f'Apellido_Paterno: {record["apellido_paterno"]}')
                print(f'Apellido_Materno: {record["apellido_materno"]}')
                print(f'Fecha_Nacimiento: {record["fecha_nacimiento"]}')
                print(f'DNI: {record["dni"]}')
                print(f'Correo: {record["correo"]}')
                print(f'Telefono: {record["telefono"]}')
                print(f'Estado: {record["estado"]}')
                print('=====================')
                
        except Exception as e:
            print(str(e))
    
    def one_alumno(self,id):
        try:    
            id = {
                '_id' : ObjectId(id)
            }
            records = self.conn.get_one(self.collection,id)

            print(f'ID: {records["_id"]}')
            print(f'Nombres: {records["nombres"]}')
            print(f'Apellido_Paterno: {records["apellido_paterno"]}')
            print(f'Apellido_Materno: {records["apellido_materno"]}')
            print(f'Fecha_Nacimiento: {records["fecha_nacimiento"]}')
            print(f'DNI: {records["dni"]}')
            print(f'Correo: {records["correo"]}')
            print(f'Telefono: {records["telefono"]}')
            print(f'Estado: {records["estado"]}')
            print('=====================')
            return records
        except Exception as ex:
            print(ex)
    
    def insert_alumno(self, data):
        
        try:  
            self.conn.insert(self.collection, data)
            print(f'se registro correctamente al alumno')

        except Exception as ex:
            print(ex)


    def update_alumno(self, id_object, data):

        try:
            id_object = {
            '_id' : ObjectId(id_object)
            }
            self.conn.update(self.collection, id_object, data)
        except Exception as ex:
            print(f'error al actualizar estudiante. Error Code: {str(ex)}')            
        return True

    def inhabilitar_alumno(self, id_object):

        try:
            id_object = {
            '_id' : ObjectId(id_object)
            }
            data = {
                'estado' : 'false'
            }
            self.conn.update(self.collection, id_object, data)
        except Exception as ex:
            print(f'error al actualizar estudiante. Error Code: {str(ex)}') 
        return True

    def alumnos_habilitados(self):

        try:
            condition = {
                'estado' :  'true'
            }
            records = self.conn.get_all_by(self.collection,condition)

            for record in records:
                    print('=================================')
                    print(f'ID: {record["_id"]}')
                    print(f'Nombres: {record["nombres"]}')
                    print(f'Apellido_Paterno: {record["apellido_paterno"]}')
                    print(f'Apellido_Materno: {record["apellido_materno"]}')
                    print(f'Fecha_Nacimiento: {record["fecha_nacimiento"]}')
                    print(f'DNI: {record["dni"]}')
                    print(f'Correo: {record["correo"]}')
                    print(f'Telefono: {record["telefono"]}')
                    print(f'Estado: {record["estado"]}')
                    print('=================================')
                    
        except Exception as ex:
            print(str(ex))
