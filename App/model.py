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
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------


def newCatalog():
    """ Inicializa el catálogo de libros

    Crea una lista vacia para guardar todos los libros

    Se crean indices (Maps) por los siguientes criterios:
    Autores
    ID libros
    Tags
    Año de publicacion

    Retorna el catalogo inicializado.
    """
    catalog = {'movies': None,
               'id': None,
               'production_companies': None,}
    catalog['movies'] = lt.newList('SINGLE_LINKED',compareIds)
    catalog['id'] = mp.newMap(2000,4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMovieMoviesIds)
    catalog['otros'] = mp.newMap(2000,4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMovieMoviesIds)
    catalog['production_companies'] = mp.newMap(2000,4001,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareProductionCompaniesByName)
    catalog["genres"] = mp.newMap(400,802,maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=comparegenres)
    catalog["production_countries"]= mp.newMap(400,802,maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareCountries)
    return catalog




# Funciones para agregar informacion al catalogo



# ==============================
# Funciones de consulta
# ==============================
def moviesSize(catalog):
    """
    Número de libros en el catago
    """
    return lt.size(catalog["production_companies"])
def getMoviesByProductionComapnie(catalog, production_companie_name):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    production_companie = mp.get(catalog['production_companies'], production_companie_name)
    if production_companie:
        return me.getValue(production_companie)
    return None
def getMoviesByGender(catalog, gender_name):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    gender_name = mp.get(catalog['genres'], gender_name)
    if gender_name:
        return me.getValue(gender_name)
    return None
def getMoviesByCountrie(catalog, countrie_name):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    countrie_name = mp.get(catalog['production_countries'], countrie_name)
    if countrie_name:
        return me.getValue(countrie_name)
    return None






# ==============================
# Funciones de Comparacion
# ==============================

def comparegenres(keyname, genres):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    compentry = me.getKey(genres)
    if (keyname == compentry):
         return 0
    elif (keyname > compentry):
         return 1
    else:
         return -1
def compareMovieMoviesIds(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1



def compareProductionCompaniesByName(keyname, production_companie):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    compentry = me.getKey(production_companie)
    if (keyname == compentry):
        return 0
    elif (keyname > compentry):
        return 1
    else:
        return -1
def compareIds(id1, id2):
    """
    Compara dos ids de libros
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareCountries(keyname, production_countries):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    compentry = me.getKey(production_countries)
    if (keyname == compentry):
         return 0
    elif (keyname > compentry):
         return 1
    else:
         return -1

def addProductionCompanie(catalog, production_companie_name, movie):
    """
    Esta función adiciona un libro a la lista de libros publicados
    por un autor.
    Cuando se adiciona el libro se actualiza el promedio de dicho autor
    """
    existproduction_companies = mp.contains( catalog['production_companies'],production_companie_name)
    if existproduction_companies:
        entry = mp.get( catalog['production_companies'],production_companie_name)
        companie = me.getValue(entry)
    else:
        companie = newProductionCompanie(production_companie_name)
        mp.put( catalog['production_companies'], production_companie_name, companie)
    lt.addLast(companie['movies'],movie )
        
    production_companieavg = (companie['vote_average'])
    movieavg = (movie['vote_average'])
    if (production_companieavg == 0.0):
        companie['vote_average'] = float(movieavg)
    else:
        companie['vote_average'] = ( production_companieavg + float(movieavg)) / 2

def add_genre(catalog,gender_name,movie):
    genres =str(gender_name).split("|")
    for  gender_name in genres:
        existgender = mp.contains( catalog['genres'],gender_name)
        if existgender:
            entry = mp.get( catalog['genres'],gender_name)
            gender= me.getValue(entry)
        else:
            gender= newgender(gender_name)
            mp.put( catalog['genres'], gender_name, gender)
        lt.addLast(gender['movies'],movie )
        
        gendcount = (gender['vote_count'])
        moviecount = (movie['vote_count'])
        if (gendcount == 0.0):
            gender['vote_count'] = float(moviecount)
        else:
            gender['vote_count'] = ( gendcount + float(moviecount)) / 2
def addCountrie(catalog, countrie_name, movie):
    """
    Esta función adiciona un libro a la lista de libros publicados
    por un autor.
    Cuando se adiciona el libro se actualiza el promedio de dicho autor
    """
    existCountrie = mp.contains( catalog['production_countries'],countrie_name)
    if existCountrie:
        entry = mp.get( catalog['production_countries'],countrie_name)
        countrie = me.getValue(entry)
    else:
        countrie = newProductionCountrie(countrie_name)
        mp.put( catalog['production_countries'], countrie_name, countrie)
    lt.addLast(countrie['movies'],movie )


def addMovie(catalog, movie):
    """
    Esta funcion adiciona un libro a la lista de libros,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Finalmente crea una entrada en el Map de años, para indicar que este
    libro fue publicaco en ese año.
    """
    lt.addLast(catalog['movies'], movie)
    mp.put(catalog['id'], movie['id'], movie)

def addMovieCasting (catalog,movie):
    mp.put(catalog['otros'], movie['id'], movie)
    
def newProductionCompanie(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    companie = {'name': "", "movies":None,"vote_average": 0}
    companie['name'] = name
    companie['movies'] = lt.newList('SINGLE_LINKED', compareProductionCompaniesByName)
    return companie
def newProductionCountrie(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    countrie = {'name': "", "movies":None}
    countrie['name'] = name
    countrie['movies'] = lt.newList('SINGLE_LINKED', compareCountries)
    return countrie

def newgender(name):
    gender = {'name': "", "movies":None,"vote_count": 0}
    gender['name'] = name
    gender['movies'] = lt.newList('SINGLE_LINKED', comparegenres)
    return gender
def moviesSize(catalog):
    """
    Número de libros en el catago
    """
    return mp.size(catalog['movies'])




