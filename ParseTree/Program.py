from Scanner import Scanner
from Core import Core
from .Decl_seq import Decl_seq
from .Stmt_seq import Stmt_seq
from .SemanticCheck import SemanticCheck
from .Memory import Memory

class Program:

    def __init__(self, scanner, data):
        self.stmt = None
        self.decl = None
        self.scanner = scanner
        self.check = SemanticCheck()
        self.check.stackEntry()
        self.memory = Memory(self.check)
        self.data = data

    def parse(self):
        if self.scanner.currentToken() == Core.PROGRAM:
            self.printToken(self.scanner.currentToken().name.lower()+"\n")
            self.scanner.nextToken()
            if self.scanner.currentToken() == Core.INT or self.scanner.currentToken() == Core.REF:
                self.decl = Decl_seq(self.scanner, 1, self.check)
                self.decl.parse()
                self.check.stackEntry()
            if self.scanner.currentToken() == Core.BEGIN:
                self.printToken(self.scanner.currentToken().name.lower()+"\n")
                self.scanner.nextToken()
                self.stmt = Stmt_seq(self.scanner, 1, self.check, self.memory, self.data)
                self.stmt.parse()
                if self.scanner.currentToken() == Core.END:
                    self.printToken(self.scanner.currentToken().name.lower())
                    self.scanner.nextToken()
                    if self.scanner.currentToken() != Core.EOS:
                        print("\nERROR: Statement after end token.")
                else:
                    print("\nERROR: Expecting END token, received " + self.scanner.currentToken().name)
                    exit(0)
            else:
                print("\nERROR: Expecting BEGIN token, received " + self.scanner.currentToken().name)
                exit(0)
        else:
            print("\nERROR: Expecting PROGRAM token, received " + self.scanner.currentToken().name)
            exit(0)

    def printToken(self, token):
        print(token, end="")

    def execute(self):
        if self.decl is not None:
            newL = self.decl.execute()
            for i in newL[0]:
                self.memory.addStatic(i, False)
            for i in newL[1]:
                self.memory.addStatic(i, True)
        self.stmt.execute()

