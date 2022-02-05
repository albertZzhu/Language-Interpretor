from Core import Core
from Scanner import Scanner
from .Decl_int import Decl_int
from .Decl_ref import Decl_ref


class Decl:

    def __init__(self, scanner, numIndent):
        self.scanner = scanner
        self.numIndent = numIndent

    def parse(self):
        if self.scanner.currentToken() == Core.INT:
            new = Decl_int(self.scanner, self.numIndent)
            new.parse()
        elif self.scanner.currentToken() == Core.REF:
            new = Decl_ref(self.scanner, self.numIndent)
            new.parse()
        else:
            print("ERROR: wrong decl format, it is neither REF nor INT")
            exit(0)

