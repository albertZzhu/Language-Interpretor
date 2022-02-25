from Core import Core
from Scanner import Scanner
from .Decl import Decl
from .Assign import Assign
from .If import If
from .Loop import Loop
from .In import In
from .Out import Out
from .SemanticCheck import SemanticCheck


class Stmt:

    def __init__(self, scanner, numIndent, check, memory, data):
        self.scanner = scanner
        self.numIndent = numIndent
        self.check = check
        self.memory = memory
        self.new = None
        self.status = -1
        self.data = data

    def parse(self):
        if self.scanner.currentToken() == Core.ID:
            self.new = Assign(self.scanner, self.numIndent, self.check, self.memory)
            self.new.parse()
            self.status = 0
        elif self.scanner.currentToken() == Core.IF:
            self.check.stackEntry()
            self.memory.pushStack()
            self.new = If(self.scanner, self.numIndent, self.check,  self.memory, self.data)
            self.new.parse()
            self.status = 1
        elif self.scanner.currentToken() == Core.WHILE:
            self.check.stackEntry()
            self.new = Loop(self.scanner, self.numIndent, self.check, self.memory, self.data)
            self.new.parse()
            self.status = 2
        elif self.scanner.currentToken() == Core.INPUT:
            self.new = In(self.scanner, self.numIndent, self.check, self.memory, self.data)
            self.new.parse()
            self.status = 3
        elif self.scanner.currentToken() == Core.OUTPUT:
            self.new = Out(self.scanner, self.numIndent, self.check, self.memory)
            self.new.parse()
            self.status = 4
        elif self.scanner.currentToken() == Core.INT or self.scanner.currentToken() == Core.REF:
            self.new = Decl(self.scanner, self.numIndent, self.check)
            self.new.parse()
            self.status = 5
        else:
            print("\nERROR: Expecting statement token form, received " + self.scanner.currentToken().name)
            exit(0)


    def printToken(self, token):
        print(token, end="")

    def execute(self):
        if self.status == 0:
            self.new.execute()
        elif self.status == 1:
            self.memory.pushStack()
            self.new.execute()
        elif self.status == 2:
            self.memory.pushStack()
            self.new.execute()
        elif self.status == 3:
            self.new.execute()
        elif self.status == 4:
            self.new.execute()
        elif self.status == 5:
            newL = self.new.execute()
            for i in newL[0]:
                self.memory.addLocal(i, False)
            for i in newL[1]:
                self.memory.addLocal(i, True)

