from Core import Core
from Scanner import Scanner
from .Cond import Cond
from .SemanticCheck import SemanticCheck


class Loop:

    def __init__(self, scanner, numIndent, check, memory, data):
        self.scanner = scanner
        self.numIndent = numIndent
        self.check = check
        self.memory = memory
        self.cond = None
        self.stmtSeq = None
        self.data = data

    def parse(self):
        from .Stmt_seq import Stmt_seq
        if self.scanner.currentToken() == Core.WHILE:
            self.printToken("\t" * self.numIndent+self.scanner.currentToken().name.lower())
            self.scanner.nextToken()
            self.cond = Cond(self.scanner, self.check, self.memory)
            self.cond.parse()
            if self.scanner.currentToken() == Core.BEGIN:
                self.printToken(" "+self.scanner.currentToken().name.lower()+"\n")
                self.scanner.nextToken()
                self.stmtSeq = Stmt_seq(self.scanner, self.numIndent+1, self.check, self.memory, self.data)
                self.stmtSeq.parse()
                if self.scanner.currentToken() == Core.ENDWHILE:
                    self.printToken("\t" * self.numIndent+self.scanner.currentToken().name.lower()+"\n")
                    self.scanner.nextToken()
                else:
                    print("\nERROR: ENDWHILE token expected, received" + self.scanner.currentToken().name)
                    exit(0)
            else:
                print("\nERROR: BEGIN token expected, received" + self.scanner.currentToken().name)
                exit(0)
        else:
            print("\nERROR: WHILE token expected, received" + self.scanner.currentToken().name)
            exit(0)
        self.check.stackExit()

    def printToken(self, token):
        print(token+" ", end="")

    def execute(self):
        while self.cond.execute():
            self.stmtSeq.execute()
            print("x: "+str(self.memory.getValue("x"))+"y: "+str(self.memory.getValue("y")))
        self.memory.popStack()

