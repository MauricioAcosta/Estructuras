from sys import stdin
import sys
sys.path.append("..")
from Pila import *
import re
#!/usr/bin/python3
# -*- coding: utf-8 -*-
from sys import stdin
import sys
sys.path.append("..")
from Pila import *
import re

class Nodo:
    def __init__(self , valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolPosFijo:

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

    def construirArbol(self, posfijo):
        # posfijo.pop()
        # variable=posfijo.pop()
        pilaOperador = Pila()
        #Recorra todo el string
        for caracter in posfijo :

            # si NO es operador lo apila
            if self.logic(caracter):
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


    def imprimirTablaTokens(self,l1 , l2):
        a = 0
        for m in l1:
            print(l1[a] + "   " + l2[a])
            a = a+1
        print("--*--*--*--*--")


def main():
    expresion=stdin.readline().split()
    arbol = ArbolPosFijo()
    arbol.construirArbol(expresion)
    # arbol.imprimirTablaTokens()




if __name__ == '__main__':
    main()

# def logic(expresion):
#     aux=-1
#     expre=[]
#     terminal=[]
#     for _ in range(len(expresion)):
#         print(expresion[aux])
#         if re.match('^[-+]?[0-9]+$', expresion[aux]):
#             # print("Numero", expresion[aux])
#             terminal.append(expresion[aux])
#             aux-=1
#         elif re.match('^[a-zA-Z_][a-zA-Z0-9_]*$', expresion[aux]):
#             terminal.append(expresion[aux])
#             # print("Variable",expresion[aux])
#             aux-=1
#         elif re.match('[-|=|+|*|/]',expresion[aux]):
#             expre.append(expresion[aux])
#             # print("signo",expresion[aux])
#             aux-=1
