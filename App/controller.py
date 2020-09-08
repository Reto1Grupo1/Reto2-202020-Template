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
