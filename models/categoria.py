from time import sleep
from repository.repo_categoria import CategoriaRepo

class Categoria:
    
    #CONSTRUCTOR
    def __init__(self):
        self.categoriaRepo = CategoriaRepo()

    #INTERFAZ CON EL USUARIO
    def interfazCategoria(self):
        try:
            print('''
            =============================
            =MODULO GESTOR PARA CATEGORIAS=
            =============================
            INDICAR QUE ACCION DESEA REALIZAR:
            1 -> REGISTAR UNA NUEVA CATEGORIA
            2 -> LISTAR CATEGORIAS REGISTRADAS
            3 -> DESHABILITAR CATEGORIA
            4 -> ACTUALIZAR CATEGORIA
            5 -> SALIR DEL SISTEMA
            ''')

            respuesta = input(">>>")

            if respuesta == "1":
                self.registar_categoria()
            elif respuesta == "2":
                self.listCategoria()
            elif respuesta == "3":
                self.deshabilitar_categoria()
            elif respuesta == "4":
                self.actualizar_categoria()
            elif respuesta == "5":
                print("SALIENDO DEL SISTEMA ......")
                sleep(2)
                exit()
        except Exception as ex:
            print(str(ex))

    def registar_categoria(self):

        try:
            print('''REGISTRO DE CATEGORIA
                POR FAVOR INGRESE UNA DESCRIPCION
            ''')
            descripcion = input(">>Ingresar descripcion de la Categoria: >> ")
            registro = {
                'descripcion' : descripcion,
                'estado' : True
            }
            self.categoriaRepo.insert_categoria(registro)
            sleep(2)
            print("volviendo al menu Categorias")
            print("3")
            sleep(1)
            print("2")
            sleep(1)
            print("...")
            self.interfazCategoria()

        except Exception as ex:
            print(f'Error al registrar la Categoria. Error code: {str(ex)}')

    def listCategoria(self):
        self.categoriaRepo.all_categorias()

    def actualizar_categoria(self):
       
        try:
            print("*****************************************************")
            print("             LISTAR CATEGORIAS A MODIFICAR              ")
            print("*****************************************************")
            self.categoriaRepo.all_categorias()
            id = input("Ingrese el ID de la Categoria a modificar: \n>>> ")
            categoria = self.categoriaRepo.one_categoria(id)
            print("MODIFICAR LOS CAMPOS REQUERIDOS \n")
            descipcion = input(f'Descripcion: {categoria["descripcion"]} >> ')
            estado = input(f'Estado: {categoria["estado"]} >> ')
            registro = {
                'descripcion' : descipcion,
                'estado' : estado
            }
            self.categoriaRepo.update_categoria(id, registro)
            print("Se actualizaron los datos correctamente!")

        except Exception as ex:
            print(f'Error al actualizar datos de la Categoria. Error code: {str(ex)}')

    def deshabilitar_categoria(self):
        try:
            print("******************************************")
            print("       LISTA DE CATEGORIAS REGISTRADOS       ")
            self.categoriaRepo.categorias_habilitados()
            print("******************************************")
            id = input(f'POR FAVOR INGRESE EL ID DE LA CATEGORIA A INHABILITAR\n >')
            self.categoriaRepo.inhabilitar_categoria(id)
            print(f'Categoria indentificado con ID: {id} fue inhabilitado correctamente')
        except Exception as ex:
            print(f'Error al inhabilitar la Categoria, error code: {str(ex)}')


