from Core import Core
from Scanner import Scanner
from .Term import Term
from .SemanticCheck import SemanticCheck


class Expr:

    def __init__(self, scanner, check):
        self.scanner = scanner
        self.check = check

    def parse(self):
        new = Term(self.scanner, self.check)
        new.parse()
        if self.scanner.currentToken() == Core.ADD:
            self.printToken("+")
            self.scanner.nextToken()
            new = Expr(self.scanner, self.check)
            new.parse()
        elif self.scanner.currentToken() == Core.SUB:
            self.printToken("-")
            self.scanner.nextToken()
            new = Expr(self.scanner, self.check)
            new.parse()

    def printToken(self, token):
        print(token, end="")