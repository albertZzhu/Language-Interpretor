from Core import Core
from .Expr import Expr

class Out:

    def __init__(self, scanner, numIndent):
        self.scanner = scanner
        self.numIndent = numIndent

    def parse(self):
        if self.scanner.currentToken() == Core.OUTPUT:
            self.printToken("\t" * self.numIndent+self.scanner.currentToken().name.lower()+" ")
            self.scanner.nextToken()
            new = Expr(self.scanner)
            new.parse()
            if self.scanner.currentToken() == Core.SEMICOLON:
                self.printToken(";\n")
                self.scanner.nextToken()
            else:
                print("ERROR: SEMICOLON token expected, received" + self.scanner.currentToken().name)
                exit(0)
        else:
            print("ERROR: INPUT token expected, received" + self.scanner.currentToken().name)
            exit(0)

    def printToken(self, token):
        print(token, end="")