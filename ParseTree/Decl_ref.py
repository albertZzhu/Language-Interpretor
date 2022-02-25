from Scanner import Scanner
from Core import Core
from .Id_list import Id_list
from .SemanticCheck import SemanticCheck



class Decl_ref:

    def __init__(self, scanner, numIndent, check):
        self.scanner = scanner
        self.numIndent = numIndent
        self.check = check
        self.newList = []

    def parse(self):
        if self.scanner.currentToken() == Core.REF:
            self.printToken(self.scanner.currentToken().name.lower())
            self.scanner.nextToken()
            new = Id_list(self.scanner)
            self.newList = new.parse()
            for i in self.newList:
                if self.check.ifREFDuplicate(i):
                    print("\nERROR: REF declare duplication: " + str(i))
                    exit(0)
            self.check.joinREF(self.newList)
        else:
            print("\nERROR: not an ref identifier")
            exit(0)

    def printToken(self, token):
        print("\t" * self.numIndent, end="")
        print(token+" ", end="")

    def execute(self):
        return self.newList


