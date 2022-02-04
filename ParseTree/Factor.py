from Core import Core
from Scanner import Scanner
from .Expr import Expr

class Factor:

    def __init__(self, scanner):
        self.scanner = scanner

    def parse(self):
        if self.scanner.currentToken() == Core.ID:
            self.printToken(self.scanner.getID())
            self.scanner.nextToken()
        elif self.scanner.currentToken() == Core.CONST:
            self.printToken(self.scanner.getCONST())
            self.scanner.nextToken()
        else:
            new = Expr(self.scanner)
            new.parse()




    def printToken(self, token):
        print(token+" ", end="")

