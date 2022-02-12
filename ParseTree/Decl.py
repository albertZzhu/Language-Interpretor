from Core import Core
from Scanner import Scanner
from .Decl_int import Decl_int
from .Decl_ref import Decl_ref
from .SemanticCheck import SemanticCheck



class Decl:

    def __init__(self, scanner, numIndent, check):
        self.scanner = scanner
        self.numIndent = numIndent
        self.check = check

    def parse(self):
        if self.scanner.currentToken() == Core.INT:
            new = Decl_int(self.scanner, self.numIndent, self.check)
            new.parse()
        elif self.scanner.currentToken() == Core.REF:
            new = Decl_ref(self.scanner, self.numIndent, self.check)
            new.parse()
        else:
            print("\nERROR: wrong decl format, it is neither REF nor INT")
            exit(0)

