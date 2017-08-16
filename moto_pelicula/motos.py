#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from cola import *
import random

class Motorcycles:
    def __init__(self,marca,cylinder,color):
        self.marca=marca
        self.cylinder=cylinder
        self.color=color

cola = Cola()

cola.encolar(Motorcycles("Pulsar",200,"amarilla"))
cola.encolar(Motorcycles("AKT",125,"negra"))
cola.encolar(Motorcycles("Kawasaki",300,"blanca"))
cola.encolar(Motorcycles("BMW",1200,"gris"))


while cola.es_vacia() == False:
    print cola.desencolar().cylinder
print "termine"

print "La cola esta vacia:",cola.es_vacia()
