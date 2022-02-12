from Core import Core
from Scanner import Scanner
from .Decl import Decl
from .SemanticCheck import SemanticCheck


class Decl_seq:

    def __init__(self, scanner, numIndent, check):
        self.scanner = scanner
        self.numIndent = numIndent
        self.check = check

    def parse(self):
        if self.scanner.currentToken() == Core.INT or self.scanner.currentToken() == Core.REF:
            new = Decl(self.scanner, self.numIndent, self.check)
            new.parse()
            if self.scanner.currentToken() == Core.INT or self.scanner.currentToken() == Core.REF:
                new = Decl_seq(self.scanner, self.numIndent, self.check)
                new.parse()
        else:
            print("\nERROR: wrong decl_seq format, it is neither REF nor INT")
            exit(0)

