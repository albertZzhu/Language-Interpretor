from Core import Core
from Scanner import Scanner
from .Factor import Factor
from .SemanticCheck import SemanticCheck


class Term:

    def __init__(self, scanner, check):
        self.scanner = scanner
        self.check = check

    def parse(self):
        new = Factor(self.scanner, self.check)
        new.parse()
        if self.scanner.currentToken() == Core.MULT:
            self.printToken("*")
            self.scanner.nextToken()
            new = Term(self.scanner, self.check)
            new.parse()

    def printToken(self, token):
        print(token, end="")
