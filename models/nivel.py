from time import sleep
from repository.repo_nivel import NivelRepo

class Nivel:
    
    #CONSTRUCTOR
    def __init__(self):
        self.nivelRepo = NivelRepo()

    #INTERFAZ CON EL USUARIO
    def interfazNivel(self):
        try:
            print('''
            =============================
            =MODULO GESTOR PARA NIVELES=
            =============================
            INDICAR QUE ACCION DESEA REALIZAR:
            1 -> REGISTAR UNA NUEVA NIVELES
            2 -> LISTAR NIVELES REGISTRADAS
            3 -> DESHABILITAR NIVELES
            4 -> ACTUALIZAR NIVELES
            5 -> SALIR DEL SISTEMA
            ''')

            respuesta = input(">>>")

            if respuesta == "1":
                self.registar_nivel()
            elif respuesta == "2":
                self.listNivel()
            elif respuesta == "3":
                self.deshabilitar_nivel()
            elif respuesta == "4":
                self.actualizar_nivel()
            elif respuesta == "5":
                print("SALIENDO DEL SISTEMA ......")
                sleep(2)
                exit()
        except Exception as ex:
            print(str(ex))

    def registar_nivel(self):

        try:
            print('''REGISTRO DE NIVELES
                POR FAVOR INGRESE UNA DESCRIPCION
            ''')
            descripcion = input(">>Ingresar descripcion de la Nivel: >> ")
            registro = {
                'nivel' : descripcion,
                'estado' : True
            }
            self.nivelRepo.insert_nivel(registro)
            sleep(2)
            print("volviendo al menu Nivels")
            print("3")
            sleep(1)
            print("2")
            sleep(1)
            print("...")
            self.interfazNivel()

        except Exception as ex:
            print(f'Error al registrar la Nivel. Error code: {str(ex)}')

    def listNivel(self):
        self.nivelRepo.all_niveles()

    def actualizar_nivel(self):
       
        try:
            print("*****************************************************")
            print("             LISTAR NIVELES A MODIFICAR              ")
            print("*****************************************************")
            self.nivelRepo.all_niveles()
            id = input("Ingrese el ID de la Nivel a modificar: \n>>> ")
            nivel = self.nivelRepo.one_nivel(id)
            print("MODIFICAR LOS CAMPOS REQUERIDOS \n")
            descipcion = input(f'Descripcion: {nivel["descripcion"]} >> ')
            estado = input(f'Estado: {nivel["estado"]} >> ')
            registro = {
                'nivel' : descipcion,
                'estado' : estado
            }
            self.nivelRepo.update_nivel(id, registro)
            print("Se actualizaron los datos correctamente!")

        except Exception as ex:
            print(f'Error al actualizar datos de la Nivel. Error code: {str(ex)}')

    def deshabilitar_nivel(self):
        try:
            print("******************************************")
            print("       LISTA DE NIVELES REGISTRADOS       ")
            self.nivelRepo.niveles_habilitados()
            print("******************************************")
            id = input(f'POR FAVOR INGRESE EL ID DE LA NIVELES A INHABILITAR\n >')
            self.nivelRepo.inhabilitar_nivel(id)
            print(f'Nivel indentificado con ID: {id} fue inhabilitado correctamente')
        except Exception as ex:
            print(f'Error al inhabilitar la Nivel, error code: {str(ex)}')


