﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # analyzer es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    return analyzer


# Funciones para la carga de datos

def loadData(analyzer):

    """
    Carga los datos de los archivos csv al catalogo
    """
    vertices = loadVertices(analyzer)
    pais = loadCountrys(analyzer)
    loadConnections(analyzer)

    return vertices, pais 
    
    


def loadConnections(analyzer):
    """
    Se crea un arco entre cada par de vertices que
    pertenecen al mismo landing_point y van en el mismo sentido.

    addRouteConnection crea conexiones entre diferentes cables
    servidas en un mismo landing_point.
    """

    servicesfile = cf.data_dir + 'connections.csv'
    input_file = csv.DictReader(open(servicesfile, encoding="utf-8"),
                                delimiter=",")
    
    
    None


def loadVertices(analyzer):
    """
    Carga los vertices del archivo.
    """

    etiquetasfile = cf.data_dir + 'landing_points.csv'
    input_file = csv.DictReader(open(etiquetasfile, encoding='utf-8'))
    cont = 0
    primerVertice = None
    for vertice in input_file:
        cont +=1
        model.mapVertice(analyzer, vertice)
        if cont == 1:
            primerVertice = vertice 
    return primerVertice
        

def loadCountrys(analyzer):
    
    """
    Carga los paises del archivo.
    """

    etiquetasfile = cf.data_dir + 'countries.csv'
    input_file = csv.DictReader(open(etiquetasfile, encoding='utf-8'))
    ultimo = None
    for country in input_file:
        model.addCountry(analyzer, country)
        ultimo = country 
    return ultimo


# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def totalLandingPoints(analyzer):
    """
    Retorna el numero de paises unicos
    """
    cont = model.numeroPaises(analyzer)
    return cont

def numeroPoints(analyzer):
    """
    Retorna el numero de landing points
    """
    cont = model.numeroPoints(analyzer)
    return cont


