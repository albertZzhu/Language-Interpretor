from Scanner import Scanner
from Core import Core
from Decl_seq import Decl_seq

class Program:

    def __init__(self, scanner):
        self.scanner = scanner

    def parse(self):
        if self.scanner.currentToken() == Core.PROGRAM:
            self.scanner.nextToken()
            new = Decl_seq(self.scanner, 1)
            new.parse()
            self.scanner.nextToken()


