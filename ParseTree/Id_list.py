from Scanner import Scanner
from Core import Core

class Id_list:

    def __init__(self, scanner):
        self.scanner = scanner

    def parse(self):
        if self.scanner.currentToken() == Core.ID:
            self.printToken(self.scanner.getID())
            self.scanner.nextToken()
            if self.scanner.currentToken() == Core.COMMA:
                self.printToken(", ")
                self.scanner.nextToken()
                new = Id_list(self.scanner)
                new.parse()
            elif self.scanner.currentToken() == Core.SEMICOLON:
                self.printToken(";\n")
        else:
            print("ERROR: not an valid ID")

    def printToken(self, token):
        print(token, end="")
