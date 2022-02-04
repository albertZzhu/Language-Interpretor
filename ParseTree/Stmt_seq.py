from Core import Core
from Scanner import Scanner
from Stmt import Stmt


class Stmt_seq:

    def __init__(self, scanner, numIndent):
        self.scanner = scanner
        self.numIndent = numIndent

    def parse(self):
        new = Stmt(self.scanner, self.numIndent)
        new.parse()
