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
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as mp
"""                                     
|   
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________
moviescastingfile="MoviesCastingRaw-small.csv"
moviesdetailsfile="SmallMoviesDetailsCleaned.csv"
moviesdetails = 'SmallMoviesDetailsCleaned.csv'
#tagsfile = 'GoodReads/themoviesdb/tags.csv'
#booktagsfile = 'GoodReads/book_tags-small.csv'





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
def printGenderData(genres):
    """
    Imprime los libros de un autor determinado
    """
    if genres:
        print('Género encontrado: ' + str(genres['name']))
        print('Promedio: ' + str(genres['vote_count']))
        print('Total de peliculas: ' + str(lt.size(genres['movies'])))
        iterator = it.newIterator(genres['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            print('Titulo: ' + movie['original_title'] )
    else:
        print('No se encontro el género')

def printCountrieData(countrie,cont):
    """
    Imprime los libros de un autor determinado
    """
    if countrie:
        print('País encontrado: ' + str(countrie['name']))
        print('Total de peliculas: ' + str(lt.size(countrie['movies'])))
        iterator = it.newIterator(countrie['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            ide=movie["id"]
            entry = mp.get( cont['otros'],ide)
            companie = me.getValue(entry)
            director= (companie["director_name"])
            print('Titulo: ' + movie['original_title'] +", Lanzamiento: " +movie["release_date"] +", Director: "+ director)
    
    else:
        print('No se encontro el País')
# ___________________________________________________
#  Menu principal
# ___________________________________________________
def printMenu():
    
    print("Bienvenido")
    print("0- Inicializar Catálogo")
    print("0.1- Cargar información en el catálogo")
    print("1- Consultar peliculas por productora") 
    print("2- Conocer un director")
    print("3- Cononocer un actor")
    print("4- Consultar peliculas por género")
    print("5- Encontrar películas por país")
    print("9- Salir")


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if float(inputs) == 0:
        print("Inicializando Catálogo ....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.initCatalog()

    elif float(inputs) == 0.1:

        print("Cargando información de los archivos ....")
        inicio=time.perf_counter()
        controller.loadData(cont, moviesdetails,moviescastingfile)
        fin=time.perf_counter()
        print("Tiempo de ejecucucion",fin-inicio)
        print('Peliculas  cargadas: ' + str(controller.moviessSize(cont)))
    

    elif int(inputs[0]) == 1:
        
        production_companie_name = input("Nombre de la companía a buscar: ")
        inicio=time.perf_counter()
        production_companieinfo = controller.getMoviesByProductionCompanie(cont, production_companie_name)
        printProductionCompanieData(production_companieinfo)
        fin=time.perf_counter()
        print("Tiempo que tomo",fin - inicio)
        #print(cont["production_companies"])
    elif int(inputs[0]) == 2:
        x
    elif int(inputs[0]) == 3:
        x
    elif int(inputs[0]) == 4:
        gender_name = input("Nombre del género que desea consultar:")
        inicio=time.perf_counter()
        gender_info = controller.getMoviesByGender(cont, gender_name)
        printGenderData(gender_info)
        fin=time.perf_counter()
        print("Tiempo que tomo",fin - inicio)
    

    elif int(inputs[0]) == 5:
        countrie_name = input("Nombre del país que desea consultar:")
        inicio=time.perf_counter()
        countrie_info = controller.getMoviesByCountrie(cont, countrie_name)
        printCountrieData(countrie_info,cont)
        fin=time.perf_counter()
    else:
        sys.exit(9)
sys.exit(9)
