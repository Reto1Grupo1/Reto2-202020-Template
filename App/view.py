"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller as controller
assert config
import time

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________
<<<<<<< HEAD
moviescastingfile="Data/themoviesdb/MoviesCastingRaw-small.csv"
moviesdetailsfile="Data/themoviesdb/SmallMoviesDetailsCleaned.csv"
=======
moviesdetails = 'themoviesdb/SmallMoviesDetailsCleaned.csv'
#tagsfile = 'GoodReads/themoviesdb/tags.csv'
#booktagsfile = 'GoodReads/book_tags-small.csv'

>>>>>>> j.caceresc




# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________

def printProductionCompanieData(production_companies):
    """
    Imprime los libros de un autor determinado
    """
    if production_companies:
        print('Productora encontrada: ' + str(production_companies['name']))
        print('Promedio: ' + str(production_companies['vote_average']))
        print('Total de peliculas: ' + str(lt.size(production_companies['movies'])))
        iterator = it.newIterator(production_companies['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            print('Titulo: ' + movie['original_title'] )
    else:
        print('No se encontro la productora')

# ___________________________________________________
#  Menu principal
# ___________________________________________________
def printMenu():
<<<<<<< HEAD
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Ranking de peliculas")
    print("3- Conocer un director")
    print("4- Conocer un actor")
    print("5- Entender un genero")
    print("6- Crear ranking")
    print("0- Salir")

def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados
    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """


    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:

            if int(inputs[0])==1: #opcion 1
                print("Cargando información de los archivos ....")
                listacasting,listadetails=controller.loadData(moviesdetailsfile,moviescastingfile)
                print("El número de películas cargadas fueron "+str(controller.moviessize(listadetails)))
                print("\nPrimer Elemento:")
                print(controller.firstelement(listadetails))
                print("\nUltimo Elemento:")
                print(controller.lastelement(listadetails))
            elif int(inputs[0])==2: #opcion 2
                pass

            elif int(inputs[0])==3: #opcion 3
                pass

            elif int(inputs[0])==4: #opcion 4
                pass

            elif int(inputs[0])==3: #opcion 5
                pass

            elif int(inputs[0])==4: #opcion 6
                pass


            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()
=======
    print("Bienvenido")
    print("1- Inicializar Catálogo")
    print("2- Cargar información en el catálogo")
    print("3- Consultar los libros de un año")
    print("4- Consultar los libros de un autor")
    print("5- Consultar los Libros por etiqueta")
    print("0- Salir")


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.initCatalog()

    elif int(inputs[0]) == 2:

        print("Cargando información de los archivos ....")
        inicio=time.perf_counter()
        controller.loadData(cont, moviesdetails)
        fin=time.perf_counter()
        print("Tiempo de ejecucucion",fin-inicio)
        print('Peliculas  cargadas: ' + str(controller.moviessSize(cont)))
    elif int(inputs[0]) == 3:
        number = input("Buscando libros del año?: ")
        books = controller.getBooksYear(cont, int(number))
        printBooksbyYear(books)
        #print(cont["production_companies"])

    elif int(inputs[0]) == 4:
        production_companie_name = input("Nombre de la companía a buscar: ")
        production_companieinfo = controller.getMoviesByProductionCompanie(cont, production_companie_name)
        printProductionCompanieData(production_companieinfo)
        #print(cont["production_companies"])

    elif int(inputs[0]) == 5:
        label = input("Etiqueta a buscar: ")
        books = controller.getBooksByTag(cont, label)
        printBooksbyTag(books)
    else:
        sys.exit(0)
sys.exit(0)
>>>>>>> j.caceresc
