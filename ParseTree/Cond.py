from Core import Core
from .Cmpr import Cmpr

class Cond:

    def __init__(self, scanner):
        self.scanner = scanner

    def parse(self):
        if self.scanner.currentToken() == Core.NEGATION:
            self.printToken(self.scanner.currentToken().name)
            self.scanner.nextToken()
            if self.scanner.currentToken() == Core.LPAREN:
                self.printToken(self.scanner.currentToken().name)
                self.scanner.nextToken()
                new = Cond(self.scanner)
                new.parse()
                if self.scanner.currentToken() == Core.RPAREN:
                    self.printToken(self.scanner.currentToken().name)
                    self.scanner.nextToken()
                else:
                    print("ERROR: RPAREN token expected, received" + self.scanner.currentToken().name)
            else:
                print("ERROR: LPAREN token expected, received" + self.scanner.currentToken().name)
        else:
            new = Cmpr(self.scanner)
            new.parse()
            if self.scanner.currentToken() == Core.OR:
                self.printToken(self.scanner.currentToken().name)
                self.scanner.nextToken()
                new = Cond(self.scanner)
                new.parse()

    def printToken(self, token):
        print(token + " ", end="")


