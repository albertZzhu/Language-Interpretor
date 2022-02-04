from Core import Core
from Scanner import Scanner
from .Decl import Decl


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
            new = While(self.scanner, self.numIndent)
            new.parse()
        elif self.scanner.currentToken() == Core.INPUT:
            new = Input(self.scanner, self.numIndent)
            new.parse()
        elif self.scanner.currentToken() == Core.OUTPUT:
            new = Output(self.scanner, self.numIndent)
            new.parse()
        elif self.scanner.currentToken() == Core.INT or self.scanner.currentToken() == Core.REF:
            new = Decl(self.scanner, self.numIndent)
            new.parse()
        else:
            print("ERROR: Expecting statement token form, received" + self.scanner.currentToken().name)


    def printToken(self, token):
        print(token, end="")