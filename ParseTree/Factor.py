from Core import Core
from Scanner import Scanner
from .SemanticCheck import SemanticCheck



class Factor:

    def __init__(self, scanner, check):
        self.scanner = scanner
        self.check = check

    def parse(self):
        from .Expr import Expr
        if self.scanner.currentToken() == Core.ID:
            if not (self.check.ifIDExist(self.scanner.getID()) or self.check.ifREFExist(self.scanner.getID())):
                print("\nERROR: ID: " + self.scanner.getID() + " not declared")
                exit(0)
            self.printToken(self.scanner.getID())
            self.scanner.nextToken()
        elif self.scanner.currentToken() == Core.CONST:
            self.printToken(str(self.scanner.getCONST()))
            self.scanner.nextToken()
        else:
            if self.scanner.currentToken() == Core.LPAREN:
                self.printToken("(")
                self.scanner.nextToken()
                new = Expr(self.scanner, self.check)
                new.parse()
                if self.scanner.currentToken() == Core.RPAREN:
                    self.printToken(")")
                    self.scanner.nextToken()
                else:
                    print("\nERROR: Expecting RPAREN received " + self.scanner.currentToken().name)
                    exit(0)
            else:
                print("\nERROR: Expecting LPAREN received " + self.scanner.currentToken().name)
                exit(0)





    def printToken(self, token):
        print(token, end="")

