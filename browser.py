import ply.lex as lex
import ply.yacc as yacc
import html_lexer
import javascript_lexer
import html_parser
import graphics as graphics
import htmlinterp

htmllexer = lex.lex(module=html_lexer) 
htmlparser = yacc.yacc(module=html_parser,tabmodule="parsetabhtml") 
ast = htmlparser.parse(webpage,lexer=htmllexer) 
jslexer = lex.lex(module=javascript_lexer)
graphics.initialize() 
htmlinterp.interpret(ast) 
graphics.finalize() 