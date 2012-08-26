import graphics
import ply.lex as lex
import ply.yacc as yacc
import jstokens
import jsgrammar

def interpret(trees): # Hello, friend
    for tree in trees: # Hello,
        # ("word-element","Hello")
        nodetype=tree[0] # "word-element"
        if nodetype == "word-element":
            graphics.word(tree[1]) 
        elif nodetype == "tag-element":
            # <b>Strong text</b>
            tagname = tree[1] # b
            tagargs = tree[2] # []
            subtrees = tree[3] # ...Strong Text!...
            closetagname = tree[4] # b
            if(tagname!=closetagname):
                graphics.warning("mismatched tag")
            else:
                graphics.begintag(tagname,tagargs)
                interpret(subtrees)
                graphics.endtag()
        elif nodetype == "javascript-element":
            jstext = tree[1]; # "document.write(55);"
            jslexer = lex.lex(module=jstokens)
            jsparser = yacc.yacc(module=jsgrammar)
            jstree = jsparser.parse(jstext,lexer=jslexer)
            # jstree is a parse tree for JavaScript
            result = jsinterp.interpret(jstree)
            graphics.word(result)