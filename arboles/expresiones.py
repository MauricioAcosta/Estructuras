#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from sys import stdin
sys.path.append("..")
from Pila import *

class Nodo:
	def __init__(self , valor):
		self.valor = valor
		self.izquierda = None
		self.derecha = None

class ArbolPosFijo:
	diccionario={}
	def buscarOperador(self, caracter):
		if (caracter == '+' or caracter == '-' or caracter == '*' or caracter == '/'):
			return 1
		elif(type(caracter)==int):
			return 2
		else:
			return 0

	def construirDiccionario(self,indice,valor):
	    self.diccionario[indice]=[valor]
	def getValorDiccionario(self,indice):
	    return self.diccionario.get(indice)


	def evaluar(self, arbol):
		if arbol.valor=='+':
			return self.evaluar(arbol.izquierda)+self.evaluar(arbol.derecha)
		if arbol.valor=='-':
			return self.evaluar(arbol.izquierda)-self.evaluar(arbol.derecha)
		if arbol.valor=='*':
			return self.evaluar(arbol.izquierda)*self.evaluar(arbol.derecha)
		if arbol.valor=='/':
			try:
				return self.evaluar(arbol.izquierda)/self.evaluar(arbol.derecha)
			except ZeroDivisionError:
				print("No esta permitida la division entre cero")
				sys.exit()
		try:
			return float(arbol.valor)
		except:
			return (self.getValorDiccionario(arbol.valor))[0]



	def construirArbol(self, posfijo):
		posfijo.pop()
		variable=posfijo.pop()
		pilaOperador = Pila()

		for caracter in posfijo:
			if self.buscarOperador(caracter)!=1:
				arbol = Nodo(caracter)
				pilaOperador.apilar(arbol)

			else:
				arbol = Nodo(caracter)
                arbol1 = pilaOperador.desapilar()
                arbol2 = pilaOperador.desapilar()
                arbol.derecha = arbol1
                arbol.izquierda = arbol2
                pilaOperador.apilar(arbol)

        #el ultimo elemento de la pila sera el arbol
		arbol = pilaOperador.desapilar()
		self.construirDiccionario(variable,self.evaluar(arbol))
		return self.evaluar(arbol)

def main():

    while True:
        obj = ArbolPosFijo()
        expresion = stdin.readline().split()
        if not expresion:
            break
        print "Valor resultante es: "+ str(obj.construirArbol(expresion))
        print "diccionario valor A "+ str(obj.getValorDiccionario('A'))
        print "diccionario valor B "+ str(obj.getValorDiccionario('B'))
        print "diccionario valor C "+ str(obj.getValorDiccionario('C'))

if __name__ == '__main__':
    main()
