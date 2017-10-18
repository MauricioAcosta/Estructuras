import ply.lex as lex

tokens = [ 'VARIABLE','NUMERO','ARITMETICOS','ASIGNACION','COMPARACIONES','CONDICIONALES','CICLOS','LOGICOS']

t_ignore = ' \t\n'
t_ARITMETICOS = r'[-+*/%]'
t_CONDICIONALES= r'^si|entonces:*|finsi*|.*sino:?'
t_LOGICOS = r'y|o|no*'
t_VARIABLE = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_ASIGNACION = r'='
t_COMPARACIONES = r'>|<|>=|<=|!=|==]'
t_CICLOS=r'mientras|.*finmientras?'


def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer
archivo=open('ejemplo.txt','r')
linea=archivo.readline()
while linea != '':
    lex.input(linea)
    while True:
        tok = lex.token()
        if not tok: break
        print str(tok.value) + " - " + str(tok.type)
    linea=archivo.readline()

"""lex.input("x = 3 - 4 + 5 * 6")"""
