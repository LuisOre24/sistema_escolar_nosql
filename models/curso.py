from time import sleep

from bson.objectid import ObjectId
from repository.repo_curso import CursoRepo

class Curso:
    
    #CONSTRUCTOR
    def __init__(self):
        self.cursoRepo = CursoRepo()

    #INTERFAZ CON EL USUARIO
    def interfazCurso(self):
        try:
            print('''
            =============================
            =MODULO GESTOR PARA CURSOS=
            =============================
            INDICAR QUE ACCION DESEA REALIZAR:
            1 -> REGISTAR UN NUEVO CURSO
            2 -> LISTAR CURSOS REGISTRADOS
            3 -> DESHABILITAR CURSO
            4 -> ACTUALIZAR CURSO
            5 -> SALIR DEL SISTEMA
            ''')

            respuesta = input(">>>")

            if respuesta == "1":
                self.registar_curso()
            elif respuesta == "2":
                self.listCurso()
            elif respuesta == "3":
                self.deshabilitar_curso()
            elif respuesta == "4":
                self.actualizar_curso()
            elif respuesta == "5":
                print("SALIENDO DEL SISTEMA ......")
                sleep(2)
                exit()
        except Exception as ex:
            print(str(ex))

    def registar_curso(self):
        try:
            print('''REGISTRO DE CURSOS
                POR FAVOR INGRESE EL NOMBRE DEL CURSO
            ''')
            nombre = input(">>Ingresar el nombre del Curso: >>> ")
            id_categoria = input(">>Ingresar la categoria del Curso: >>> ")
            registro = {
                'curso' : nombre,
                'categoria' : {
                                '_id' : ObjectId(id_categoria)
                            },
                'estado' : True
            }
            self.cursoRepo.insert_curso(registro)
            sleep(2)
            print("volviendo al menu Cursos")
            print("3")
            sleep(1)
            print("2")
            sleep(1)
            print("...")
            self.interfazCurso()
        except Exception as ex:
            print(f'Error al registrar al Curso. Error code: {str(ex)}')

    def listCurso(self):
        self.cursoRepo.all_cursos()

    def actualizar_curso(self):
        try:
            print("*****************************************************")
            print("             LISTAR CURSOS A MODIFICAR              ")
            print("*****************************************************")
            self.cursoRepo.all_cursos()
            id = input("Ingrese el ID del Curso a modificar: \n>>> ")
            curso = self.cursoRepo.one_curso(id)
            print("MODIFICAR LOS CAMPOS REQUERIDOS \n")
            nombres = input(f'Curso: {curso["descripcion"]} >>> ')
            categoria = input(f'Categoria: {curso["categoria"]} >>> ')
            estado = input(f'Estado: {curso["estado"]} >>> ')
            registro = {
                'curso' : nombres,
                'categoria' : {
                    '_id' : ObjectId(categoria)
                },
                'estado' : estado
            }
            self.cursoRepo.update_curso(id, registro)
            print("Se actualizaron los datos correctamente!")

        except Exception as ex:
            print(f'Error al actualizar datos del Curso. Error code: {str(ex)}')

    def deshabilitar_curso(self):
        try:
            print("******************************************")
            print("       LISTA DE CURSOS REGISTRADOS       ")
            self.cursoRepo.cursos_habilitados()
            print("******************************************")
            id = input(f'POR FAVOR INGRESE EL ID DEL CURSO A INHABILITAR > ')
            self.cursoRepo.inhabilitar_curso(id)
            print(f'Curso indentificado con ID: {id} fue inhabilitado correctamente')
        except Exception as ex:
            print(f'Error al inhabilitar al curso, error code: {str(ex)}')


