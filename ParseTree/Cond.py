from Core import Core
from .Cmpr import Cmpr
from .SemanticCheck import SemanticCheck


class Cond:

    def __init__(self, scanner, check):
        self.scanner = scanner
        self.check = check

    def parse(self):
        if self.scanner.currentToken() == Core.NEGATION:
            self.printToken("!")
            self.scanner.nextToken()
            if self.scanner.currentToken() == Core.LPAREN:
                self.printToken("(")
                self.scanner.nextToken()
                new = Cond(self.scanner, self.check)
                new.parse()
                if self.scanner.currentToken() == Core.RPAREN:
                    self.printToken(")")
                    self.scanner.nextToken()
                else:
                    print("\nERROR: RPAREN token expected, received" + self.scanner.currentToken().name)
                    exit(0)
            else:
                print("\nERROR: LPAREN token expected, received" + self.scanner.currentToken().name)
                exit(0)
        else:
            new = Cmpr(self.scanner, self.check)
            new.parse()
            if self.scanner.currentToken() == Core.OR:
                self.printToken(self.scanner.currentToken().name)
                self.scanner.nextToken()
                new = Cond(self.scanner, self.check)
                new.parse()

    def printToken(self, token):
        print(token, end="")


