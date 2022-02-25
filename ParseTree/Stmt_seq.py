from Core import Core
from Scanner import Scanner
from .Stmt import Stmt
from .SemanticCheck import SemanticCheck


class Stmt_seq:

    def __init__(self, scanner, numIndent, check, memory, data):
        self.scanner = scanner
        self.numIndent = numIndent
        self.check = check
        self.memory = memory
        self.newStmt = None
        self.newStmtSeq = None
        self.data = data

    def parse(self):
        self.newStmt = Stmt(self.scanner, self.numIndent, self.check, self.memory, self.data)
        self.newStmt.parse()
        if self.scanner.currentToken() != Core.END \
                and self.scanner.currentToken() != Core.ENDIF \
                and self.scanner.currentToken() != Core.ELSE \
                and self.scanner.currentToken() != Core.ENDWHILE:
            self.newStmtSeq = Stmt_seq(self.scanner, self.numIndent, self.check, self.memory, self.data)
            self.newStmtSeq.parse()

    def execute(self):
        self.newStmt.execute()
        if self.newStmtSeq is not None:
            self.newStmtSeq.execute()
