from Core import Core
from Scanner import Scanner
from .Term import Term

class Expr:

    def __init__(self, scanner):
        self.scanner = scanner

    def parse(self):
        new = Term(self.scanner)
        new.parse()
        if self.scanner.currentToken() == Core.ADD:
            self.printToken("+")
            self.scanner.nextToken()
            new = Expr(self.scanner)
            new.parse()
        elif self.scanner.currentToken() == Core.SUB:
            self.printToken("-")
            self.scanner.nextToken()
            new = Expr(self.scanner)
            new.parse()

    def printToken(self, token):
        print(token, end="")