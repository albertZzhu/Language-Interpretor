from Core import Core
from Scanner import Scanner
from .Decl import Decl
from .Assign import Assign
from .If import If
from .Loop import Loop
from .In import In
from .Out import Out
from .SemanticCheck import SemanticCheck


class Stmt:

    def __init__(self, scanner, numIndent, check):
        self.scanner = scanner
        self.numIndent = numIndent
        self.check = check

    def parse(self):
        if self.scanner.currentToken() == Core.ID:
            new = Assign(self.scanner, self.numIndent, self.check)
            new.parse()
        elif self.scanner.currentToken() == Core.IF:
            self.check.stackEntry()
            new = If(self.scanner, self.numIndent, self.check)
            new.parse()
        elif self.scanner.currentToken() == Core.WHILE:
            self.check.stackEntry()
            new = Loop(self.scanner, self.numIndent, self.check)
            new.parse()
        elif self.scanner.currentToken() == Core.INPUT:
            new = In(self.scanner, self.numIndent, self.check)
            new.parse()
        elif self.scanner.currentToken() == Core.OUTPUT:
            new = Out(self.scanner, self.numIndent, self.check)
            new.parse()
        elif self.scanner.currentToken() == Core.INT or self.scanner.currentToken() == Core.REF:
            new = Decl(self.scanner, self.numIndent, self.check)
            new.parse()
        else:
            print("\nERROR: Expecting statement token form, received " + self.scanner.currentToken().name)
            exit(0)


    def printToken(self, token):
        print(token, end="")