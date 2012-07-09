import ply.lex as lex

states=(
        ('jscomment','exclusive'),
        )
tokens = (
        'ANDAND',       # &&
        'COMMA',        # ,
        'DIVIDE',       # /
        'ELSE',         # else
        'EQUAL',        # =
        'EQUALEQUAL',   # ==
        'FALSE',        # false
        'FUNCTION',     # function
        'GE',           # >=
        'GT',           # >
        'IDENTIFIER',   # charater a-zA-Z followed by any num of a-zA-Z_
        'IF',           # if
        'LBRACE',       # {
        'LE',           # <=
        'LPAREN',       # (
        'LT',           # <
        'MINUS',        # -
        'NOT',          # !
        'NUMBER',       # any number i.e. 13.0,13. but not 12.1.2 - token value is floating point value
        'OROR',         # ||
        'PLUS',         # +
        'RBRACE',       # }
        'RETURN',       # return
        'RPAREN',       # )
        'SEMICOLON',    # ;
        'STRING',       #"any characters including escaped quotes i.e. \"" 
        'TIMES',        # *
        'TRUE',         # true
        'VAR',          # var
)
t_ignore = ' \t\v\r' # whitespace 
t_jscomment_ignore=' \t\v\r'
def t_IDENTIFIER(t):
    r'[a-zA-Z]+[a-zA-Z_]*'
    return t
def t_NUMBER(t):
    r'[-]?[0-9]+[\.]?[0-9]*'
    t.value = float(t.value)
    return t
def t_STRING(t):
    r'["](:?[^"]|[\\"])+["]'
    t.value = t.value[1:-1]
    return t
def t_jsonelinecomment(t):
    r'//.*'
    pass

def t_jscomment(t):
    r'\/\*'
    t.lexer.begin('jscomment')

def t_jscomment_end(t):
    r'\*\/'
    t.lexer.lineno += t.value.count('\n')
    t.lexer.begin('INITIAL')
    pass

def t_jscomment_error(t):
        t.lexer.skip(1)
def t_ANDAND(t):
    r'&&'
    return t
def t_COMMA(t):
    r','
    return t
def t_DIVIDE(t):
    r'/'
    return t

def t_ELSE(t):
    r'else'
    return t
def t_EQUALEQUAL(t):
    r'=='
    return t

def t_EQUAL(t):
    r'='
    return t

def t_FALSE(t):
    r'false'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_GE(t):
    r'>='
    return t

def t_GT(t):
    r'>'
    return t

def t_IF(t):
    r'if'
    return t

def t_LBRACE(t):
    r'{'
    return t

def t_LE(t):
    r'<='
    return t

def t_LPAREN(t):
    r'\('
    return t

def t_LT(t):
    r'<'
    return t

def t_MINUS(t):
    r'-'
    return t

def t_NOT(t):
    r'!'
    return t

def t_OROR(t):
    r'\|\|'
    return t

def t_PLUS(t):
    r'\+'
    return t

def t_RBRACE(t):
    r'}'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_RPAREN(t):
    r'\)'
    return t

def t_SEMICOLON(t):
    r';'
    return t

def t_TIMES(t):
    r'\*'
    return t

def t_TRUE(t):
    r'true'
    return t

def t_VAR(t):
    r'var'
    return t


t_ignore                = ' \t\v\r' # whitespace 

def t_newline(t):
        r'\n'
        t.lexer.lineno += 1

def t_error(t):
        print "JavaScript Lexer: Illegal character " + t.value[0]
        t.lexer.skip(1)
