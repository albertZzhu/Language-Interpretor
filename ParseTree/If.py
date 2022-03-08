from Core import Core
from Scanner import Scanner
from .Cond import Cond
from .SemanticCheck import SemanticCheck


class If:

    def __init__(self, scanner, numIndent, check, memory, data):
        self.scanner = scanner
        self.numIndent = numIndent
        self.check = check
        self.memory = memory
        self.cond = None
        self.stmtSeq1 = None
        self.stmtSeq2 = None
        self.status = 0
        self.data = data

    def parse(self):
        from .Stmt_seq import Stmt_seq
        if self.scanner.currentToken() == Core.IF:
            self.scanner.nextToken()
            self.cond = Cond(self.scanner, self.check, self.memory)
            self.cond.parse()
            if self.scanner.currentToken() == Core.THEN:
                self.scanner.nextToken()
                self.stmtSeq1 = Stmt_seq(self.scanner, self.numIndent+1, self.check, self.memory, self.data)
                self.stmtSeq1.parse()
                if self.scanner.currentToken() == Core.ENDIF:
                    self.scanner.nextToken()
                elif self.scanner.currentToken() == Core.ELSE:
                    self.status = 1
                    self.scanner.nextToken()
                    self.stmtSeq2 = Stmt_seq(self.scanner, self.numIndent+1, self.check, self.memory, self.data)
                    self.stmtSeq2.parse()
                    if self.scanner.currentToken() == Core.ENDIF:
                        self.scanner.nextToken()
                    else:
                        print("\nERROR: ELSE token expected, received" + self.scanner.currentToken().name)
                        exit(0)
                else:
                    print("\nERROR: ENDIF or ELSE token expected, received" + self.scanner.currentToken().name)
                    exit(0)
            else:
                print("\nERROR: THEN token expected, received" + self.scanner.currentToken().name)
                exit(0)
        else:
            print("\nERROR: If token expected, received" + self.scanner.currentToken().name)
            exit(0)
        self.check.stackExit()

    def printToken(self, token):
        print(token+" ", end="")

    def execute(self):
        if self.cond.execute():
            self.stmtSeq1.execute()
        else:
            if self.status == 1:
                self.stmtSeq2.execute()
        self.memory.popStack()
