from Core import Core
from Scanner import Scanner
from .Decl import Decl
from .SemanticCheck import SemanticCheck


class Decl_seq:

    def __init__(self, scanner, numIndent, check):
        self.scanner = scanner
        self.numIndent = numIndent
        self.check = check
        self.tempList=[]
        self.decl = None
        self.declSeq = None

    def parse(self):
        if self.scanner.currentToken() == Core.INT or self.scanner.currentToken() == Core.REF:
            self.decl = Decl(self.scanner, self.numIndent, self.check)
            self.decl.parse()
            if self.scanner.currentToken() == Core.INT or self.scanner.currentToken() == Core.REF:
                self.declSeq = Decl_seq(self.scanner, self.numIndent, self.check)
                self.declSeq.parse()
        else:
            print("\nERROR: wrong decl_seq format, it is neither REF nor INT")
            exit(0)

    def execute(self):
        self.tempList = self.decl.execute()
        if self.declSeq is not None:
            new = self.declSeq.execute()
            self.tempList[0].extend(new[0])
            self.tempList[1].extend(new[1])
        return self.tempList



