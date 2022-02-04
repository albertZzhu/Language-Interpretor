from Core import Core
from .Expr import Expr

class Cmpr:

    def __init__(self, scanner):
        self.scanner = scanner

    def parse(self):
        new = Expr(self.scanner)
        new.parse()
        if self.scanner.currentToken() == Core.EQUAL:
            self.printToken(self.scanner.currentToken().name)
            self.scanner.nextToken()
            new = Expr(self.scanner)
            new.parse()
        elif self.scanner.currentToken() == Core.LESS:
            self.printToken(self.scanner.currentToken().name)
            self.scanner.nextToken()
            new = Expr(self.scanner)
            new.parse()
        elif self.scanner.currentToken() == Core.LESSEQUAL:
            self.printToken(self.scanner.currentToken().name)
            self.scanner.nextToken()
            new = Expr(self.scanner)
            new.parse()
        else:
            print("ERROR: EQUAL or LESS or LESSEQUAL token expected, received" + self.scanner.currentToken().name)


    def printToken(self, token):
        print(token + " ", end="")