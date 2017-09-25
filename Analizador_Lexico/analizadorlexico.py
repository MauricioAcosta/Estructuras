import ply.lex as lex
import re
import codecs
import os
import sys

tokens = ['ID','NUMBER','PLUS','MINUS','TIMES','DIVIDE',
          'ODD', 'ASSIGN','ASSING','ME','LT','LTE','GT',
          'GTE','LPARENT','RPARENT','COMMA','SEMMICOLOM',
          'DDT','UPDATE'
          ]
reservadas = {
          'begin':'BEGIN',
          'end':'END',
          'if':'IF',
          'then':'THEN',
          'while':'WHILE',
          'do':'DO',
          'call':'CALL',
          'const':'CONST',
          'int':'INT',
          'procedure':'PROCEDURE',
          'out':'OUT',
          'in':'IN',
          'else':'ELSE',
}

tokens = tokens + list(reservadas.values())

t_ignore = '\t'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_ODD = r'ODD'
t_ASSING = r'='
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLOM = r';'
t_DDT = r'\.'
t_UPDATE = r':='

def t_ID(token):
          #reconocer las variables
          r'[a-zA-Z_][a-zA-Z0-9_]*'
          if token.value.upper() in keywords:
                    token.value = t.value.upper()
                    token.type = t.value
          return token

def t_COMMENT(token):
          #reconocer un comentario
          r'\#.*'
          pass
def t_NUMBER(token):
          #reconocer los numeros solo enteros
          r'\d+'
          token.value = int(t.value)
          return t
def t_error(token):
          print ("caracter ilegal '%s'" % token.value[0])
          token.lexer.sikip(1)

def buscarFicheros(directorio):
          ficheros = []
          numArchivo = ''
          respuesta= False
          cont = 1

          for base, dirs, files in os.walk(directorio):
                    ficheros.append(files)

          for file in files:
                    print (str(cont)+ ". "+file )
                    cont = cont+1

          while respuesta == False:
                    numArchivo = raw_input('\nNumero del test: ')
                    for file in files:
                              if file == files[int(numArchivo)-1]:
                                        respuesta = True
                                        break
          print "Has escogido \"%s\"\n" % %files[int(numArchivo)-1]
          return files[int(numArchivo)-1]

#directorio donde se encuentran los archivos de prueba
#lo puedes encontrar facilmente parandote sobre el directorio en una terminal con pwd
directorio = '/home/gnome/Estructuras/test/'
archivo = buscarFicheros(directorio)
test = directorio+archivo
fileopen = codecs.open(test,'r','utf-8')
cadena = fileopen.read()
fileopen.close()

analizador.input(cadena)

while True:
          token = analiador.token()
          if not token:
                    break
          print (token)
