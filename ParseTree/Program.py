from Scanner import Scanner
from Core import Core
from Decl_seq import Decl_seq
from Stmt_seq import Stmt_seq

class Program:

    def __init__(self, scanner):
        self.scanner = scanner

    def parse(self):
        if self.scanner.currentToken() == Core.PROGRAM:
            self.printToken(self.scanner.currentToken().name)
            self.scanner.nextToken()
            if self.scanner.currentToken() == Core.INT or self.scanner.currentToken() == Core.REF:
                new = Decl_seq(self.scanner, 1)
                new.parse()
            if self.scanner.currentToken() == Core.BEGIN:
                self.printToken(self.scanner.currentToken().name)
                self.scanner.nextToken()
                new = Stmt_seq(self.scanner, 1)
                new.parse()
                if self.scanner.currentToken() == Core.END:
                    self.printToken(self.scanner.currentToken().name)
                else:
                    print("ERROR: Expecting END token, received " + self.scanner.currentToken().name)
                    exit(0)
            else:
                print("ERROR: Expecting BEGIN token, received " + self.scanner.currentToken().name)
                exit(0)
        else:
            print("ERROR: Expecting PROGRAM token, received " + self.scanner.currentToken().name)
            exit(0)

    def printToken(self, token):
        print(token, end="")

