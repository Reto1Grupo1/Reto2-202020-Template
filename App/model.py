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
from time import process_time
import csv
"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------
def loadCSVFile (file, sep=";"):

    #lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    lst = lt.newList("SINGLE_LINKED") #Usando implementacion linkedlist
    dialect = csv.excel()
    dialect.delimiter=sep
    with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    return lst



# Funciones para agregar informacion al catalogo



# ==============================
# Funciones de consulta
# ==============================
def moviessize (listadetails):
    return lt.size(listadetails)


def lastelement (listadetails):
    last=lt.getElement(listadetails,moviessize(listadetails))
    infolast={}
    infolast["original_title"]=last["original_title"]
    infolast["release_date"]=last["release_date"]
    infolast["vote_average"]=last["vote_average"]
    infolast["vote_count"]=last["vote_count"]
    infolast["original_language"]=last["original_language"]
    return infolast


def firstelement (listadetails):
    first=lt.getElement(listadetails,1)
    infofirst={}
    infofirst["original_title"]=first["original_title"]
    infofirst["release_date"]=first["release_date"]
    infofirst["vote_average"]=first["vote_average"]
    infofirst["vote_count"]=first["vote_count"]
    infofirst["original_language"]=first["original_language"]
    return infofirst
# ==============================
# Funciones de Comparacion
# ==============================


