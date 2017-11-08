#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
class Nodo():
	def __init__ (self,valor,izq=None,der=None):
		self.valor=valor
		self.izquierda=izq
		self.derecha=der

def logic(caracter):
    aux=-1
    terminal=[]
    expresion=[]
    if re.match('^[-+]?[0-9]+$', caracter):
        print("Numero", caracter)
        terminal.append(caracter)
        aux-=1
    elif re.match('^[a-zA-Z_][a-zA-Z0-9_]*$', caracter):
        terminal.append(caracter)
        print("Variable",caracter)
        aux-=1
    elif re.match('[-|=|+|*|/]',caracter):
        expresion.append(caracter)
        print("signo",caracter)
        aux-=1

def postorden(arbol):
	if arbol==None:
		return ""
	else:
		return postorden(arbol.izquierda)+postorden(arbol.derecha)+arbol.valor


expresion1 = postorden(Nodo('+',Nodo('5'),Nodo('-',Nodo('8'),Nodo('6'))))
expresion2 = postorden( Nodo('+',Nodo('-',Nodo('7'),Nodo('/',Nodo('10'),Nodo('2'))),Nodo('3')) )

print expresion1

for i in expresion1:
    logic(i)

print expresion2
for i in expresion2:
    logic(i)
