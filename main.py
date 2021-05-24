from models.grado import Grado
from models.seccion import Seccion
from models.curso import Curso
from models.periodo import Periodo
from models.nivel import Nivel
from models.categoria import Categoria
from models.docente import Docente
from models.alumno import Alumno

from time import sleep

class Start():

    def __init__(self):
        try:
            print('''
            BIENVENIDO AL SISTEMA DE GESTION ESCOLAR
            ¿QUE ES LO QUE DESEA GESTIONAR?
            1 -> GESTION PARA DOCENTES
            2 -> GESTION PARA ESTUDIANTES
            3 -> GESTION DE PERIODOS
            4 -> GESTION DE NIVELES
            5 -> GESTION DE GRADOS
            6 -> GESTION DE SECCION
            7 -> GESTION DE CURSOS
            8 -> GESTION DE CATEGORIAS DE CURSOS
            9 -> SALIR DEL SISTEMA
            ''')
            opcion = input(">>")
            if opcion == "1":
                docente = Docente()
                docente.interfazDocente()
            elif opcion == "2":
                alumno = Alumno()
                alumno.interfazEstudiante()
            elif opcion == "3":
                periodo = Periodo()
                periodo.interfazPeriodo()
            elif opcion == "4":
                nivel = Nivel()
                nivel.interfazNivel()
            elif opcion == "5":
                grado = Grado()
                grado.interfazGrado()
            elif opcion == "6":
                seccion = Seccion()
                seccion.interfazSeccion()
            elif opcion == "7":
                curso = Curso()
                curso.interfazCurso()
            elif opcion == "8":
                categoria = Categoria()
                categoria.interfazCategoria()
            elif opcion == "9":
                print("Saliendo del Sistema ....")
                sleep(2)
                exit()
        except KeyboardInterrupt:
            print("\nForzando salida del sistema")
    
Start()