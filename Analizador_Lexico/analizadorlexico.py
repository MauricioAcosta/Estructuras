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

    def variablesDiccionario(self):
         for i in self.diccionario:
             print ("variable: {} --> Valor: {}".format(i,str(self.getValorDiccionario(i))))


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
                print("Error!! ---> Division entre cero")
                sys.exit()
        try:
            return float(arbol.valor)
        except:
            return (self.getValorDiccionario(arbol.valor))[0]

    def evaluarCaracteres(self, aux, l1 , l2):
        errores =0
        for x in aux:
            if re.match('^[-+]?[0-9]+$', x):
                l1.append("numero")
                l2.append(x)
            elif re.match('^[a-zA-Z_][a-zA-Z0-9_]*$', x):
                l1.append("variable")
                l2.append(x)
            elif re.match('[-|=|+|*|/]', x):
                l1.append("operador")
                l2.append(x)
            else:
                l1.append("Token No Valido")
                l2.append(x)
                errores+=1
        return errores



    def construirArbol(self, posfijo):
        posfijo.pop()
        variable=posfijo.pop()
        pilaOperador = Pila()
        #Recorra todo el string
        for caracter in posfijo :

            # si NO es operador lo apila
            if self.buscarOperador(caracter)!=1:
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
        return self.evaluar(arbol)

    def imprimirTablaTokens(self,l1 , l2):
        a = 0
        for m in l1:
            print(l1[a] + "   " + l2[a])
            a = a+1
        print("--*--*--*--*--")

def main():
    obj = ArbolPosFijo()
    err=0
    lTipo = []
    lValor = []
    while True:

      expresion = stdin.readline().split()
      if not expresion:

          print ('--*-- Variables Finales --*--')
          obj.variablesDiccionario()
          break
      print (' '.join(expresion))
      err=obj.evaluarCaracteres(expresion, lTipo, lValor)

      if(err==0):
          print ("El valor resultante es: "+ str(obj.construirArbol(expresion)))
    obj.imprimirTablaTokens(lTipo,lValor)

if __name__ == '__main__':
    main()
