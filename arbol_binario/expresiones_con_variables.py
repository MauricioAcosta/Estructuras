#!/usr/bin/python
# -*- coding: utf-8 -*-
from sys import stdin
class Nodo():
	def __init__ (self,valor,izq=None,der=None):
		self.valor=valor
		self.izquierda=izq
		self.derecha=der

def postorden(arbol):
	if arbol==None:
		return ""
	else:
		return postorden(arbol.izquierda)+postorden(arbol.derecha)+arbol.valor

def evaluar(arbol):
	if arbol.valor=='+':
		return evaluar(arbol.izquierda)+evaluar(arbol.derecha)
	elif arbol.valor=='-':
		return evaluar(arbol.izquierda)-evaluar(arbol.derecha)
	elif arbol.valor=='*':
		return evaluar(arbol.izquierda)*evaluar(arbol.derecha)
	elif arbol.valor=='/':
		return evaluar(arbol.izquierda)/evaluar(arbol.derecha)
	elif arbol.valor=='='
	else:
		return int(arbol.valor)

dic={}
while True:
	c=0
	expresion=stdin.readline().split( )

	print expresion

	if not expresion:
		break

	for i in expresion:
		dic[c]= expresion[0]
		expresion.pop(0)
		c=c+1
	print dic
