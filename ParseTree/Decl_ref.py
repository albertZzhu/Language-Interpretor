from Scanner import Scanner
from Core import Core
from .Id_list import Id_list


class Decl_ref:

    def __init__(self, scanner, numIndent):
        self.scanner = scanner
        self.numIndent = numIndent

    def parse(self):
        if self.scanner.currentToken() == Core.REF:
            self.printToken(self.scanner.currentToken().name.lower())
            self.scanner.nextToken()
            new = Id_list(self.scanner)
            new.parse()
        else:
            print("ERROR: not an ref identifier")

    def printToken(self, token):
        print("\t" * self.numIndent, end="")
        print(token+" ", end="")


