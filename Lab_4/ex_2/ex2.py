import ply.lex as lex
import ply.yacc as yacc
import sys

from lexer import *
from parser import *

# create objects MY LEXER and MY PARSER
myLex = MyLexer()
myPars = MyParser(myLex)

lex = myLex.lexer
parser = myPars.parser

# reading INPUT FILE

file = open('./myFile.txt')
parser.parse(file.read())
