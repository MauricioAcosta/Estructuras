#!/usr/bin/python
# -*- coding: utf-8 -*-
from Pila import *

class Peliculas:

    def __init__(self,year,gender,author):
        self.year=year
        self.gender=gender
        self.author=author

pila = Pila()

pila.apilar(Peliculas(2001,"fantasy","Andres"))
pila.apilar(Peliculas(2012,"romance","Hasta"))
pila.apilar(Peliculas(2010,"accion","Nicolas"))
pila.apilar(Peliculas(2001,"horror","Arnold"))

while pila.es_vacia() == False:
    print pila.desapilar().author
print "termine"
print "La pila esta vacia:",pila.es_vacia()
