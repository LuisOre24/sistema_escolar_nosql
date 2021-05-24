from time import sleep

from bson.objectid import ObjectId
from repository.repo_grado import GradoRepo

class Grado:

    def __init__(self):
        self.gradoRepo = GradoRepo()

    def interfazGrado(self):
        try:
            print('''
            =============================
            =MODULO GESTOR PARA GRADOS=
            =============================
            INDICAR QUE ACCION DESEA REALIZAR:
            1 -> REGISTAR UN NUEVO GRADO
            2 -> LISTAR GRADOS REGISTRADOS
            3 -> DESHABILITAR GRADO
            4 -> ACTUALIZAR GRADO
            5 -> SALIR DEL SISTEMA
            ''')

            respuesta = input(">>>")

            if respuesta == "1":
                self.registar_grado()
            elif respuesta == "2":
                self.listGrado()
            elif respuesta == "3":
                self.deshabilitar_grado()
            elif respuesta == "4":
                self.actualizar_grado()
            elif respuesta == "5":
                print("SALIENDO DEL SISTEMA ......")
                sleep(2)
                exit()
        except Exception as ex:
            print(str(ex))

    def registar_grado(self):
        try:
            print('''REGISTRO DE GRADOS
                POR FAVOR INGRESE EL MES Y AÑO
            ''')
            grado = input(">>Ingresar el Grado del Grado: >>> ")
            nivel = input(">>Ingresar el Nivel del Grado: >>> ")
            registro = {
                'grado' : grado,
                'nivel' : nivel,
                'estado' : True
            }
            self.gradoRepo.insert_grado(registro)
            sleep(2)
            print("volviendo al menu Grados")
            print("3")
            sleep(1)
            print("2")
            sleep(1)
            print("...")
            self.interfazGrado()
        except Exception as ex:
            print(f'Error al registrar al Curso. Error code: {str(ex)}')

    def listGrado(self):
        self.gradoRepo.all_grados()

    def actualizar_grado(self):
        try:
            print("*****************************************************")
            print("             LISTAR GRADOS A MODIFICAR              ")
            print("*****************************************************")
            self.gradoRepo.all_grados()
            id = input("Ingrese el ID del Grado a modificar: \n>>> ")
            grado = self.gradoRepo.one_grado(id)
            print("MODIFICAR LOS CAMPOS REQUERIDOS \n")
            grado = input(f'Mes: {grado["grado"]} >>> ')
            nivel = input(f'Año: {grado["nivel"]} >>> ')
            estado = input(f'Estado: {grado["estado"]} >>> ')

            registro = {
                'grado' : grado,
                'nivel' : nivel,
                'estado' : estado
            }
            self.gradoRepo.update_grado(id, registro)
            print("Se actualizaron los datos correctamente!")
        except Exception as ex:
            print(f'Error al actualizar datos del Grado. Error code: {str(ex)}')

    def deshabilitar_grado(self):
        try:
            print("******************************************")
            print("       LISTA DE GRADOS REGISTRADOS       ")
            self.gradoRepo.grados_habilitados
            print("******************************************")
            id = input(f'POR FAVOR INGRESE EL ID DEL GRADO A INHABILITAR > ')
            self.gradoRepo.inhabilitar_grado(id)
            print(f'Grado indentificado con ID: {id} fue inhabilitado correctamente')
        except Exception as ex:
            print(f'Error al inhabilitar al grado, error code: {str(ex)}')
    

