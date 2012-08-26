import ply.lex as lex
import ply.yacc as yacc
import htmltokens
import jstokens
import htmlgrammar
import graphics as graphics
import htmlinterp
import urllib

#gets page contents
def get_page(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return ""

htmllexer = lex.lex(module=htmltokens) 
htmlparser = yacc.yacc(module=htmlgrammar,tabmodule="parsetabhtml")
while True:
	url = raw_input()
	webpage = get_page(url) 
	ast = htmlparser.parse(webpage,lexer=htmllexer) 
	jslexer = lex.lex(module=jstokens)
	graphics.initialize() 
	htmlinterp.interpret(ast) 
	graphics.finalize()
	print "next!" 