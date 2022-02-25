from Core import Core
from .Expr import Expr
from .SemanticCheck import SemanticCheck


class Out:

    def __init__(self, scanner, numIndent, check, memory):
        self.scanner = scanner
        self.numIndent = numIndent
        self.check = check
        self.memory = memory
        self.expr = None

    def parse(self):
        if self.scanner.currentToken() == Core.OUTPUT:
            self.printToken("\t" * self.numIndent+self.scanner.currentToken().name.lower()+" ")
            self.scanner.nextToken()
            self.expr = Expr(self.scanner, self.check, self.memory)
            self.expr.parse()
            if self.scanner.currentToken() == Core.SEMICOLON:
                self.printToken(";\n")
                self.scanner.nextToken()
            else:
                print("\nERROR: SEMICOLON token expected, received" + self.scanner.currentToken().name)
                exit(0)
        else:
            print("\nERROR: INPUT token expected, received" + self.scanner.currentToken().name)
            exit(0)

    def printToken(self, token):
        print(token, end="")

    def execute(self):
        print("\n"+str(self.expr.execute()))
