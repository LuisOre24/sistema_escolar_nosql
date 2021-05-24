from repository.repo_docente import *
from time import sleep


class Docente:
    def __init__(self):
        self.docenteRepo = DocenteRepo()


    def interfazDocente(self):
        try:
            print('''
            =============================
            =MODULO GESTOR PARA ESTUDIANTES=
            =============================
            INDICAR QUE ACCION DESEA REALIZAR:
            1 -> REGISTAR A UN NUEVO ESTUDIANTE
            2 -> LISTAR ESTUDIANTES REGISTRADOS
            3 -> DESHABILITAR ESTUDIANTE
            4 -> ACTUALIZAR ESTUDIANTE
            5 -> SALIR DEL SISTEMA
            ''')

            respuesta = input(">>>")

            if respuesta == "1":
                self.registar_docente()
            elif respuesta == "2":
                self.listDocente()
            elif respuesta == "3":
                self.deshabilitar_docente()
            elif respuesta == "4":
                self.actualizar_docente()
            elif respuesta == "5":
                print("SALIENDO DEL SISTEMA ......")
                sleep(2)
                exit()
        except Exception as ex:
            print(str(ex))

    def registar_docente(self):

        try:
            print('''REGISTRO DE DOCENTES
                POR FAVOR INGRESE LOS NOMBRES, APELLIDOS, FECHA DE NACIMIENTO, DNI, CORREO, TELEFONO DEL DOCENTE
            ''')
            nombre = input(">>Ingresar los nombres del Docente: >>> ")
            apellido_paterno = input(">>Ingresar el apellido paterno del Docente: >>> ")
            apellido_materno = input(">>Ingresar el apellido materno del Docente: >>> ")
            fecha_nacimiento = input(">>Ingresar fecha de nacimiento (dd/mm/aaaa) del Docente: >>> ")
            dni = int(input(">>Ingresar el DNI del Docente: >>> "))
            correo = input(">>Ingresar el correo del Docente (No indispensable): >>> ")
            telefono = input(">>Ingresar el numero de telefono del Docente: >>> ")

            registro = {
                'nombres' : nombre,
                'apellido_paterno' : apellido_paterno,
                'apellido_materno' : apellido_materno,
                'fecha_nacimiento' : fecha_nacimiento,
                'dni' : dni,
                'correo' : correo,
                'telefono' : telefono,
                'estado' : True
            }

            self.docenteRepo.insert_docente(registro)
            sleep(2)
            print("volviendo al menu Docentes")
            print("3")
            sleep(1)
            print("2")
            sleep(1)
            print("...")
            self.interfazDocente()

        except Exception as ex:
            print(f'Error al registrar al Docente. Error code: {str(ex)}')

    def listDocente(self):
        self.docenteRepo.all_docentes()

    def actualizar_docente(self):
       
        try:
            print("*****************************************************")
            print("             LISTAR DOCENTES A MODIFICAR              ")
            print("*****************************************************")
            self.docenteRepo.all_docentes()
            id = input("Ingrese el ID del Docente a modificar: \n>>> ")
            
            docente = self.docenteRepo.one_docente(id)

            print("MODIFICAR LOS CAMPOS REQUERIDOS \n")

            nombres = input(f'Nombres: {docente["nombres"]} >>> ')
            apellido_paterno = input(f'Apellido Paterno: {docente["apellido_paterno"]} >>> ')
            apellido_materno = input(f'Apellido Materno: {docente["apellido_materno"]} >>> ')
            fecha_nacimiento = input(f'Fecha_Nacimiento: {docente["fecha_nacimiento"]} >>> ')
            dni = input(f'DNI: {docente["dni"]} >>> ')
            correo = input(f'Correo: {docente["correo"]} >>> ')
            telefono = input(f'Telefono: {docente["telefono"]} >>> ')
            estado = input(f'Estado: {docente["estado"]} >>> ')

            registro = {
                'nombres' : nombres,
                'apellido_paterno' : apellido_paterno,
                'apellido_materno' : apellido_materno,
                'fecha_nacimiento' : fecha_nacimiento,
                'dni' : dni,
                'correo' : correo,
                'telefono' : telefono,
                'estado' : estado
            }

            self.docenteRepo.update_docente(id, registro)
            print("Se actualizaron los datos correctamente!")

        except Exception as ex:
            print(f'Error al actualizar datos del Docente. Error code: {str(ex)}')

    def deshabilitar_docente(self):
        try:
            print("******************************************")
            print("       LISTA DE DOCENTES REGISTRADOS       ")
            self.docenteRepo.docentes_habilitados()
            print("******************************************")
            id = input(f'Ingrese el ID del docente a deshabilitar: >> ')
            self.docenteRepo.inhabilitar_docente(id)
            print(f'Docente indentificado con ID: {id} fue inhabilitado correctamente')
        except Exception as ex:
            print(f'Error al inhabilitar al docente, error code: {str(ex)}')
