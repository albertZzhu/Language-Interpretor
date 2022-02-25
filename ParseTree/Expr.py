from Core import Core
from Scanner import Scanner
from .Term import Term
from .SemanticCheck import SemanticCheck


class Expr:

    def __init__(self, scanner, check, memory):
        self.scanner = scanner
        self.check = check
        self.term = None
        self.secondExpr = None
        self.status = -1
        self.memory = memory

    def parse(self):
        self.term = Term(self.scanner, self.check, self.memory)
        self.term.parse()
        if self.scanner.currentToken() == Core.ADD:
            self.status = 0
            self.printToken("+")
            self.scanner.nextToken()
            self.secondExpr = Expr(self.scanner, self.check, self.memory)
            self.secondExpr.parse()
        elif self.scanner.currentToken() == Core.SUB:
            self.status = 1
            self.printToken("-")
            self.scanner.nextToken()
            self.secondExpr = Expr(self.scanner, self.check, self.memory)
            self.secondExpr.parse()

    def printToken(self, token):
        print(token, end="")

    def execute(self):
        value = self.term.execute()
        if self.status == 0:
            value += self.secondExpr.execute()
        elif self.status == 1:
            value -= self.secondExpr.execute()
        return value
