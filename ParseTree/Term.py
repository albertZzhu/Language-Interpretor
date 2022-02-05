from Core import Core
from Scanner import Scanner
from .Factor import Factor

class Term:

    def __init__(self, scanner):
        self.scanner = scanner

    def parse(self):
        new = Factor(self.scanner)
        new.parse()
        if self.scanner.currentToken() == Core.MULT:
            self.printToken("*")
            self.scanner.nextToken()
            new = Term(self.scanner)
            new.parse()

    def printToken(self, token):
        print(token, end="")
