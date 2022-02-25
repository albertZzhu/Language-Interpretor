from Core import Core
from Scanner import Scanner
from .Factor import Factor
from .SemanticCheck import SemanticCheck


class Term:

    def __init__(self, scanner, check, memory):
        self.scanner = scanner
        self.check = check
        self.factor = None
        self.secondTerm = None
        self.memory = memory

    def parse(self):
        self.factor = Factor(self.scanner, self.check, self.memory)
        self.factor.parse()
        if self.scanner.currentToken() == Core.MULT:
            self.printToken("*")
            self.scanner.nextToken()
            self.secondTerm = Term(self.scanner, self.check, self.memory)
            self.secondTerm.parse()

    def printToken(self, token):
        print(token, end="")

    def execute(self):
        value = self.factor.execute()
        if self.secondTerm is not None:
            value *= self.secondTerm.execute()
        return value


