from Core import Core
from Scanner import Scanner
from .SemanticCheck import SemanticCheck



class Factor:

    def __init__(self, scanner, check, memory):
        self.scanner = scanner
        self.check = check
        self.valueRef = None
        self.status = -1
        self.memory = memory

    def parse(self):
        from .Expr import Expr
        if self.scanner.currentToken() == Core.ID:
            if not (self.check.ifIDExist(self.scanner.getID()) or self.check.ifREFExist(self.scanner.getID())):
                print("\nERROR: ID: " + self.scanner.getID() + " not declared")
                exit(0)
            self.status = 0
            self.valueRef = self.scanner.getID()
            self.scanner.nextToken()
        elif self.scanner.currentToken() == Core.CONST:
            self.status = 1
            self.valueRef = self.scanner.getCONST()
            self.scanner.nextToken()
        else:
            if self.scanner.currentToken() == Core.LPAREN:
                self.scanner.nextToken()
                self.status = 2
                self.valueRef = Expr(self.scanner, self.check, self.memory)
                self.valueRef.parse()
                if self.scanner.currentToken() == Core.RPAREN:
                    self.scanner.nextToken()
                else:
                    print("\nERROR: Expecting RPAREN received " + self.scanner.currentToken().name)
                    exit(0)
            else:
                print("\nERROR: Expecting LPAREN received " + self.scanner.currentToken().name)
                exit(0)

    def printToken(self, token):
        print(token, end="")

    def execute(self):
        value = 0
        if self.status == 0:
            value = self.memory.getValue(self.valueRef)
        elif self.status == 1:
            value = self.valueRef
        elif self.status == 2:
            value = self.valueRef.execute()
        return value


