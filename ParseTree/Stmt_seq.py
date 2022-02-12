from Core import Core
from Scanner import Scanner
from .Stmt import Stmt
from .SemanticCheck import SemanticCheck


class Stmt_seq:

    def __init__(self, scanner, numIndent, check):
        self.scanner = scanner
        self.numIndent = numIndent
        self.check = check

    def parse(self):
        new = Stmt(self.scanner, self.numIndent, self.check)
        new.parse()
        while self.scanner.currentToken() != Core.END \
                and self.scanner.currentToken() != Core.ENDIF \
                and self.scanner.currentToken() != Core.ELSE \
                and self.scanner.currentToken() != Core.ENDWHILE:
            new = Stmt(self.scanner, self.numIndent, self.check)
            new.parse()
