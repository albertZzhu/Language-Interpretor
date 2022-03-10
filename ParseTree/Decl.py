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
        self.tempList=[[], []]
        self.int = None
        self.ref = None

    def parse(self):
        if self.scanner.currentToken() == Core.INT:
            self.int = Decl_int(self.scanner, self.numIndent, self.check)
            self.int.parse()
        elif self.scanner.currentToken() == Core.REF:
            self.ref = Decl_ref(self.scanner, self.numIndent, self.check)
            self.ref.parse()
        else:
            print("\nERROR: wrong decl format, it is neither REF nor INT.")
            exit(0)

    def execute(self):
        if self.int is not None:
            self.tempList[0] = self.int.execute()
        elif self.ref is not None:
            self.tempList[1] = self.ref.execute()
        return self.tempList


