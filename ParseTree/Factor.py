from Core import Core
from Scanner import Scanner


class Factor:

    def __init__(self, scanner):
        self.scanner = scanner

    def parse(self):
        from .Expr import Expr
        if self.scanner.currentToken() == Core.ID:
            self.printToken(self.scanner.getID())
            self.scanner.nextToken()
        elif self.scanner.currentToken() == Core.CONST:
            self.printToken(str(self.scanner.getCONST()))
            self.scanner.nextToken()
        else:
            if self.scanner.currentToken() == Core.LPAREN:
                self.printToken("(")
                self.scanner.nextToken()
                new = Expr(self.scanner)
                new.parse()
                if self.scanner.currentToken() == Core.RPAREN:
                    self.printToken(")")
                    self.scanner.nextToken()
                else:
                    print("ERROR: Expecting RPAREN received " + self.scanner.currentToken().name)
                    exit(0)
            else:
                print("ERROR: Expecting LPAREN received " + self.scanner.currentToken().name)
                exit(0)





    def printToken(self, token):
        print(token, end="")

