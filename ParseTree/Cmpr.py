from Core import Core
from .Expr import Expr
from .SemanticCheck import SemanticCheck


class Cmpr:

    def __init__(self, scanner, check):
        self.scanner = scanner
        self.check = check

    def parse(self):
        new = Expr(self.scanner, self.check)
        new.parse()
        if self.scanner.currentToken() == Core.EQUAL:
            self.printToken("==")
            self.scanner.nextToken()
            new = Expr(self.scanner, self.check)
            new.parse()
        elif self.scanner.currentToken() == Core.LESS:
            self.printToken("<")
            self.scanner.nextToken()
            new = Expr(self.scanner, self.check)
            new.parse()
        elif self.scanner.currentToken() == Core.LESSEQUAL:
            self.printToken("<=")
            self.scanner.nextToken()
            new = Expr(self.scanner, self.check)
            new.parse()
        else:
            print("\nERROR: EQUAL or LESS or LESSEQUAL token expected, received" + self.scanner.currentToken().name)
            exit(0)

    def printToken(self, token):
        print(token, end="")