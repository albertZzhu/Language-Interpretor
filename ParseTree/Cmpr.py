from Core import Core
from .Expr import Expr
from .SemanticCheck import SemanticCheck


class Cmpr:

    def __init__(self, scanner, check, memory):
        self.scanner = scanner
        self.check = check
        self.memory = memory
        self.baseExpr = None
        self.performExpr = None
        self.status = -1

    def parse(self):
        self.baseExpr = Expr(self.scanner, self.check, self.memory)
        self.baseExpr.parse()
        if self.scanner.currentToken() == Core.EQUAL:
            self.status = 0
            self.printToken("==")
            self.scanner.nextToken()
            self.performExpr = Expr(self.scanner, self.check, self.memory)
            self.performExpr.parse()
        elif self.scanner.currentToken() == Core.LESS:
            self.status = 1
            self.printToken("<")
            self.scanner.nextToken()
            self.performExpr = Expr(self.scanner, self.check, self.memory)
            self.performExpr.parse()
        elif self.scanner.currentToken() == Core.LESSEQUAL:
            self.status = 2
            self.printToken("<=")
            self.scanner.nextToken()
            self.performExpr = Expr(self.scanner, self.check, self.memory)
            self.performExpr.parse()
        else:
            print("\nERROR: EQUAL or LESS or LESSEQUAL token expected, received" + self.scanner.currentToken().name)
            exit(0)

    def printToken(self, token):
        print(token, end="")

    def execute(self):
        value = None
        if self.status == 0:
            value = self.baseExpr.execute() == self.performExpr.execute()
        elif self.status == 1:
            value = self.baseExpr.execute() < self.performExpr.execute()
        elif self.status == 2:
            value = self.baseExpr.execute() <= self.performExpr.execute()
        return value