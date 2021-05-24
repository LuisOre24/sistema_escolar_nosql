from time import sleep
from repository.repo_alumno import *

class Alumno:
    
    #CONSTRUCTOR
    def __init__(self):
        self.alumnoRepo = AlumnoRepo()

    #INTERFAZ CON EL USUARIO
    def interfazEstudiante(self):
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
                self.registar_alumno()
            elif respuesta == "2":
                self.listEstudiante()
            elif respuesta == "3":
                self.deshabilitar_alumno()
            elif respuesta == "4":
                self.actualizar_alumno()
            elif respuesta == "5":
                print("SALIENDO DEL SISTEMA ......")
                sleep(2)
                exit()
        except Exception as ex:
            print(str(ex))

    def registar_alumno(self):

        try:
            print('''REGISTRO DE ALUMNOS
                POR FAVOR INGRESE LOS NOMBRES, APELLIDOS, FECHA DE NACIMIENTO, DNI, CORREO, TELEFONO DEL ALUMNO
            ''')
            nombre = input(">>Ingresar los nombres del Alumno: >>> ")
            apellido_paterno = input(">>Ingresar el apellido paterno del Alumno: >>> ")
            apellido_materno = input(">>Ingresar el apellido materno del Alumno: >>> ")
            fecha_nacimiento = input(">>Ingresar fecha de nacimiento (dd/mm/aaaa) del Alumno: >>> ")
            dni = int(input(">>Ingresar el DNI del Alumno: >>> "))
            correo = input(">>Ingresar el correo del Alumno (No indispensable): >>> ")
            telefono = input(">>Ingresar el numero de telefono del Alumno: >>> ")

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

            self.alumnoRepo.insert_alumno(registro)
            sleep(2)
            print("volviendo al menu Estudiantes")
            print("3")
            sleep(1)
            print("2")
            sleep(1)
            print("...")
            self.interfazEstudiante()

        except Exception as ex:
            print(f'Error al registrar al Alumno. Error code: {str(ex)}')

    def listEstudiante(self):
        self.alumnoRepo.all_alumnos()

    def actualizar_alumno(self):
       
        try:
            print("*****************************************************")
            print("             LISTAR ALUMNOS A MODIFICAR              ")
            print("*****************************************************")
            self.alumnoRepo.all_alumnos()
            id = input("Ingrese el ID del Alumno a modificar: \n>>> ")
            
            alumno = self.alumnoRepo.one_alumno(id)

            print("MODIFICAR LOS CAMPOS REQUERIDOS \n")

            nombres = input(f'Nombres: {alumno["nombres"]} >>> ')
            apellido_paterno = input(f'Apellido Paterno: {alumno["apellido_paterno"]} >>> ')
            apellido_materno = input(f'Apellido Materno: {alumno["apellido_materno"]} >>> ')
            fecha_nacimiento = input(f'Fecha_Nacimiento: {alumno["fecha_nacimiento"]} >>> ')
            dni = input(f'DNI: {alumno["dni"]} >>> ')
            correo = input(f'Correo: {alumno["correo"]} >>> ')
            telefono = input(f'Telefono: {alumno["telefono"]} >>> ')
            estado = input(f'Estado: {alumno["estado"]} >>> ')

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

            self.alumnoRepo.update_alumno(id, registro)
            print("Se actualizaron los datos correctamente!")

        except Exception as ex:
            print(f'Error al actualizar datos del Alumno. Error code: {str(ex)}')

    def deshabilitar_alumno(self):
        try:
            print("******************************************")
            print("       LISTA DE ALUMNOS REGISTRADOS       ")
            self.alumnoRepo.alumnos_habilitados()
            print("******************************************")
            id = input(f'Ingrese el ID del alumno a deshabilitar: >> ')
            self.alumnoRepo.inhabilitar_alumno(id)

            print(f'Alumno indentificado con ID: {id} fue inhabilitado correctamente')

        except Exception as ex:
            print(f'Error al inhabilitar al alumno, error code: {str(ex)}')


