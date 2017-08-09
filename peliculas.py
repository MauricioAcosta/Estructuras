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
pila.apilar(Peliculas(2010,"accion","Niclas"))
pila.apilar(Peliculas(2001,"horror","arnold"))

print pila.es_vacia()
while pila.es_vacia() == False:
    print pila.desapilar().author
print "termine"
