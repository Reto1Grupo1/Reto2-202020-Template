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

import config as cf
from App import model
import csv



"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def loadData(moviesdetailsfile,moviescastingfile):
    """
    Carga los datos de los archivos en el modelo
    """
    listadetails=loadMoviesDetails(moviesdetailsfile)
    listacasting=loadMoviesCasting(moviescastingfile)
    return listacasting,listadetails

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalog = model.newCatalog()
    return catalog

def loadMoviesDetails (moviesdetailsfile):
    listadetails = model.loadCSVFile(moviesdetailsfile) #llamar funcion cargar datos 
    return listadetails

def loadMoviesCasting(moviescastingfile):
    listacasting = model.loadCSVFile(moviescastingfile)
    return listacasting

# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________

def moviessize(listadetails):
    """Numero de libros leido
    """
    return model.moviessize(listadetails)
def lastelement(listadetails):
    return model.lastelement(listadetails)
def firstelement(listadetails):
    return model.firstelement(listadetails)
# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
def loadData(catalog, moviesdetails,moviescastingfile):
    """
    Carga los datos de los archivos en el modelo
    """
    loadmoviesdetails(catalog, moviesdetails)
    loadcasting(catalog,moviescastingfile)


def loadcasting(catalog, castingraw):
    """
    Carga en el catalogo los tags a partir de la informacion
    del archivo de etiquetas
    """
    castingraw = cf.data_dir + castingraw
    input_file = csv.DictReader(open(castingraw, encoding='utf-8-sig'), delimiter=";")
    for movie in input_file:
        model.addMovieCasting(catalog,movie)
        model.add_director(catalog,movie["director_name"],movie["id"])
        model.addActors(catalog,movie)

def loadmoviesdetails(catalog, moviesdetails):
    """
    Carga en el catalogo los tags a partir de la informacion
    del archivo de etiquetas
    """
    moviesdetails = cf.data_dir + moviesdetails
    input_file = csv.DictReader(open(moviesdetails, encoding='utf-8-sig'), delimiter=";")
    for movie in input_file:
        model.addMovie(catalog, movie)
        model.addProductionCompanie(catalog, movie["production_companies"], movie)
        model.add_genre(catalog,movie["genres"],movie)
        model.addCountrie(catalog,movie["production_countries"],movie)
def moviessSize(catalog):
    """Numero de libros leido
    """
    return model.moviesSize(catalog)

#FUNCIONES PARA CONSULTA
def getMoviesByProductionCompanie(catalog, production_companie_name):
    """
    Retorna los libros de un autor
    """
    production_companieinfo = model.getMoviesByProductionComapnie(catalog, production_companie_name)
    return production_companieinfo
def average(catalog,production_companie_name):
    model.average(catalog,production_companie_name)
def count(catalog,gender_name):
    model.count(catalog,gender_name)
def knowDirector(catalog, director_name):
    director_info = model.knowDirector(catalog, director_name)
    return director_info

def knowr_actor(catalog,actor,Maximo):
    return model.know_actor(catalog,actor,Maximo)

def getMoviesByGender(catalog, gender_name):
    """
    Retorna los libros de un autor
    """
    gender_info = model.getMoviesByGender(catalog, gender_name)
    return gender_info

def getMoviesByCountrie(catalog, countrie_name):
    """
    Retorna los libros de un autor
    """
    countrie_info = model.getMoviesByCountrie(catalog, countrie_name)
    return countrie_info

def MayorId(castingraw):
    castingraw = cf.data_dir + castingraw
    input_file = csv.DictReader(open(castingraw, encoding='utf-8-sig'), delimiter=";")
    for movie in input_file:
        MayorId=model.Maxid(movie)
    return MayorId
