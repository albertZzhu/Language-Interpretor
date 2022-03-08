from Core import Core
from .Cmpr import Cmpr
from .SemanticCheck import SemanticCheck


class Cond:

    def __init__(self, scanner, check, memory):
        self.scanner = scanner
        self.check = check
        self.memory = memory
        self.status = -1
        self.valueRef = None
        self.newCond = None

    def parse(self):
        if self.scanner.currentToken() == Core.NEGATION:
            self.status = 0
            self.scanner.nextToken()
            if self.scanner.currentToken() == Core.LPAREN:
                self.scanner.nextToken()
                self.valueRef = Cond(self.scanner, self.check, self.memory)
                self.valueRef.parse()
                if self.scanner.currentToken() == Core.RPAREN:
                    self.scanner.nextToken()
                else:
                    print("\nERROR: RPAREN token expected, received" + self.scanner.currentToken().name)
                    exit(0)
            else:
                print("\nERROR: LPAREN token expected, received" + self.scanner.currentToken().name)
                exit(0)
        else:
            self.status = 1
            self.valueRef = Cmpr(self.scanner, self.check, self.memory)
            self.valueRef.parse()
            if self.scanner.currentToken() == Core.OR:
                self.status = 2
                self.scanner.nextToken()
                self.newCond = Cond(self.scanner, self.check, self.memory)
                self.newCond.parse()

    def printToken(self, token):
        print(token, end="")

    def execute(self):
        value = None
        if self.status == 0:
            value = not self.valueRef.execute()
        elif self.status == 1:
            value = self.valueRef.execute()
        elif self.status == 2:
            value = self.valueRef.execute() or self.newCond.execute()
        return value


