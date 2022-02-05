from Core import Core
from Scanner import Scanner
from .Decl import Decl
from .Assign import Assign
from .If import If
from .Loop import Loop
from .In import In
from .Out import Out

class Stmt:

    def __init__(self, scanner, numIndent):
        self.scanner = scanner
        self.numIndent = numIndent

    def parse(self):
        if self.scanner.currentToken() == Core.ID:
            new = Assign(self.scanner, self.numIndent)
            new.parse()
        elif self.scanner.currentToken() == Core.IF:
            new = If(self.scanner, self.numIndent)
            new.parse()
        elif self.scanner.currentToken() == Core.WHILE:
            new = Loop(self.scanner, self.numIndent)
            new.parse()
        elif self.scanner.currentToken() == Core.INPUT:
            new = In(self.scanner, self.numIndent)
            new.parse()
        elif self.scanner.currentToken() == Core.OUTPUT:
            new = Out(self.scanner, self.numIndent)
            new.parse()
        elif self.scanner.currentToken() == Core.INT or self.scanner.currentToken() == Core.REF:
            new = Decl(self.scanner, self.numIndent)
            new.parse()
        else:
            print("ERROR: Expecting statement token form, received " + self.scanner.currentToken().name)
            exit(0)


    def printToken(self, token):
        print(token, end="")