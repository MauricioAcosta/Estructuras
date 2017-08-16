#!/usr/bin/python
# -*- coding: utf-8 -*-
class Nodo():
	def __init__ (self,valor,izq=None,der=None):
		self.valor=valor
		self.izquierda=izq
		self.derecha=der

def preorden(arbol):
	if arbol==None:
		return ""
	else:
		return arbol.valor+preorden(arbol.izquierda)+preorden(arbol.derecha)

def evaluar(arbol):
	if arbol.valor=='+':
		return evaluar(arbol.izquierda)+evaluar(arbol.derecha)
	elif arbol.valor=='-':
		return evaluar(arbol.izquierda)-evaluar(arbol.derecha)
	elif arbol.valor=='*':
		return evaluar(arbol.izquierda)*evaluar(arbol.derecha)
	elif arbol.valor=='/':
		return evaluar(arbol.izquierda)/evaluar(arbol.derecha)
	else:
		return int(arbol.valor)

print (preorden(Nodo('+',Nodo('5'),Nodo('-',Nodo('8'),Nodo('6')))))
print (evaluar(Nodo('+',Nodo('5'),Nodo('-',Nodo('8'),Nodo('6')))))
