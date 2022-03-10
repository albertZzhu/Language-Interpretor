from Core import Core
from Scanner import Scanner
from .Decl import Decl
from .SemanticCheck import SemanticCheck
from .Func_decl import Func_decl


class Decl_seq:

    def __init__(self, scanner, numIndent, check, memory, data):
        self.scanner = scanner
        self.numIndent = numIndent
        self.check = check
        self.tempList = [[], []]
        self.memory = memory
        self.data = data
        self.decl = None
        self.declSeq = None
        self.func = None
        self.indi = None

    def parse(self):
        if self.scanner.currentToken() == Core.INT or self.scanner.currentToken() == Core.REF:
            self.decl = Decl(self.scanner, self.numIndent, self.check)
            self.decl.parse()
            self.indi = True
            if self.scanner.currentToken() == Core.INT \
                    or self.scanner.currentToken() == Core.REF\
                    or self.scanner.currentToken() == Core.ID:
                self.declSeq = Decl_seq(self.scanner, self.numIndent, self.check, self.memory, self.data)
                self.declSeq.parse()

        elif self.scanner.currentToken() == Core.ID:
            self.func = Func_decl(self.scanner, self.numIndent, self.check, self.memory, self.data)
            self.func.parse()
            self.indi = False
            if self.scanner.currentToken() == Core.INT \
                    or self.scanner.currentToken() == Core.REF \
                    or self.scanner.currentToken() == Core.ID:
                self.declSeq = Decl_seq(self.scanner, self.numIndent, self.check, self.memory, self.data)
                self.declSeq.parse()
        else:
            print("\nERROR: wrong decl_seq format, it is neither REF nor INT")
            exit(0)

    def execute(self):
        if self.indi:
            self.tempList = self.decl.execute()
        else:
            self.func.execute()
        if self.declSeq is not None:
            new = self.declSeq.execute()
            self.tempList[0].extend(new[0])
            self.tempList[1].extend(new[1])
        return self.tempList



