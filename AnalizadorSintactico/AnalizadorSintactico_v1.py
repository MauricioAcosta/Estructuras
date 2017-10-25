from sys import stdin
import sys
sys.path.append("..")
from Pila import *
import re

class Nodo():
	def __init__ (self,valor,izq=None,der=None):
		self.valor=valor
		self.izquierda=izq
        self.derecha=der

class ArbolPosFijo:
	diccionario={}
	# def buscarOperador(self, caracter):
    #     if caracter == '=':
    #         return 0
	# 	if (caracter == '+' or caracter == '-' or caracter == '*' or caracter == '/'):
	# 		return 1
	# 	elif(type(caracter)==int):
	# 		return 2

	def construirArbol(self, posfijo):

        # posfijo.pop()
		# variable=posfijo.pop()
		pilaOperador = Pila()
		#Recorra todo el string
		for caracter in posfijo :

			# si NO es operador lo apila
			if self.buscarOperador(caracter)==2:
				arbol = Nodo(caracter)
				pilaOperador.apilar(arbol)

			# Operador
			else:
				# desapila dos nodos
				arbol = Nodo(caracter)
				arbol1 = pilaOperador.desapilar()
				arbol2 = pilaOperador.desapilar()

				# los convierte en hijos
				arbol.derecha = arbol1
				arbol.izquierda = arbol2

				# Anade nuevo arbol a la pila
				pilaOperador.apilar(arbol)

		# Al final el ultimo elemento de la pila sera el arbol
		arbol = pilaOperador.desapilar()
		self.construirDiccionario(variable,self.evaluar(arbol))
		return arbol



def logic(expresion):
    for x in expresion:
        if re.match('^[-+]?[0-9]+$', x):
            l1.append("numero")
            l2.append(x)
        elif re.match('^[a-zA-Z_][a-zA-Z0-9_]*$', x):
            l1.append("variable")
            l2.append(x)
        elif re.match('[-|=|+|*|/]', x):
            l1.append("operador")
            l2.append(x)
        # else:
        #     l1.append("Token No Valido")
        #     l2.append(x)
        #     errores+=1

def main():
    pass

if __name__ == '__main__':
    main()
