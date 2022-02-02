from Core import Core
from Scanner import Scanner
from Decl import Decl


class Decl_seq:

    def __init__(self, scanner, numIndent):
        self.scanner = scanner
        self.numIndent = numIndent

    def parse(self):
        if self.scanner.currentToken() == Core.INT or self.scanner.currentToken() == Core.REF:
            new = Decl(self.scanner, self.numIndent)
            new.parse()
            self.scanner.nextToken()
            if self.scanner.currentToken() == Core.INT or self.scanner.currentToken() == Core.REF:
                new = Decl_seq(self.scanner, self.numIndent)
                new.parse()
        else:
            print("ERROR: wrong decl_seq format, it is neither REF nor INT")
