from time import sleep
from repository.repo_seccion import SeccionRepo

class Seccion:
    
    #CONSTRUCTOR
    def __init__(self):
        self.seccionRepo = SeccionRepo()

    #INTERFAZ CON EL USUARIO
    def interfazSeccion(self):
        try:
            print('''
            =============================
            =MODULO GESTOR PARA SECCIONS=
            =============================
            INDICAR QUE ACCION DESEA REALIZAR:
            1 -> REGISTAR UNA NUEVA SECCION
            2 -> LISTAR SECCIONS REGISTRADAS
            3 -> DESHABILITAR SECCION
            4 -> ACTUALIZAR SECCION
            5 -> SALIR DEL SISTEMA
            ''')

            respuesta = input(">>>")

            if respuesta == "1":
                self.registar_seccion()
            elif respuesta == "2":
                self.listSeccion()
            elif respuesta == "3":
                self.deshabilitar_seccion()
            elif respuesta == "4":
                self.actualizar_seccion()
            elif respuesta == "5":
                print("SALIENDO DEL SISTEMA ......")
                sleep(2)
                exit()
        except Exception as ex:
            print(str(ex))

    def registar_seccion(self):

        try:
            print('''REGISTRO DE SECCION
                POR FAVOR INGRESE UNA DESCRIPCION
            ''')
            descripcion = input(">>Ingresar descripcion de la Seccion: >> ")
            registro = {
                'seccion' : descripcion,
                'estado' : True
            }
            self.seccionRepo.insert_seccion(registro)
            sleep(2)
            print("volviendo al menu Seccions")
            print("3")
            sleep(1)
            print("2")
            sleep(1)
            print("...")
            self.interfazSeccion()

        except Exception as ex:
            print(f'Error al registrar la Seccion. Error code: {str(ex)}')

    def listSeccion(self):
        self.seccionRepo.all_secciones()

    def actualizar_seccion(self):
       
        try:
            print("*****************************************************")
            print("             LISTAR SECCIONES A MODIFICAR              ")
            print("*****************************************************")
            self.seccionRepo.all_secciones()
            id = input("Ingrese el ID de la Seccion a modificar: \n>>> ")
            seccion = self.seccionRepo.one_seccion(id)
            print("MODIFICAR LOS CAMPOS REQUERIDOS \n")
            descipcion = input(f'Descripcion: {seccion["descripcion"]} >> ')
            estado = input(f'Estado: {seccion["estado"]} >> ')
            registro = {
                'seccion' : descipcion,
                'estado' : estado
            }
            self.seccionRepo.update_seccion(id, registro)
            print("Se actualizaron los datos correctamente!")

        except Exception as ex:
            print(f'Error al actualizar datos de la Seccion. Error code: {str(ex)}')

    def deshabilitar_seccion(self):
        try:
            print("******************************************")
            print("       LISTA DE SECCIONS REGISTRADOS       ")
            self.seccionRepo.secciones_habilitados()
            print("******************************************")
            id = input(f'POR FAVOR INGRESE EL ID DE LA SECCION A INHABILITAR\n >')
            self.seccionRepo.inhabilitar_seccion(id)
            print(f'Seccion indentificado con ID: {id} fue inhabilitado correctamente')
        except Exception as ex:
            print(f'Error al inhabilitar la Seccion, error code: {str(ex)}')


