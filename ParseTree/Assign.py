from Core import Core
from Scanner import Scanner
from .Expr import Expr

class Assign:

    def __init__(self, scanner, numIndent):
        self.scanner = scanner
        self.numIndent = numIndent

    def parse(self):
        self.printToken("\t" * self.numIndent+self.scanner.getID())
        self.scanner.nextToken()
        if self.scanner.currentToken() == Core.ASSIGN:
            self.printToken("=")
            self.scanner.nextToken()
            if self.scanner.currentToken() == Core.NEW:
                self.printToken(self.scanner.currentToken().name.lower()+" ")
                self.scanner.nextToken()
                if self.scanner.currentToken() == Core.CLASS:
                    self.printToken(self.scanner.currentToken().name.lower())
                    self.scanner.nextToken()
                    if self.scanner.currentToken() == Core.SEMICOLON:
                        self.printToken(";\n")
                        self.scanner.nextToken()
                    else:
                        print("ERROR: Expecting Semicolon token, received " + self.scanner.currentToken().name.lower())
                        exit(0)
                else:
                    print("ERROR: Expecting Class token, received " + self.scanner.currentToken().name.lower())
                    exit(0)
            elif self.scanner.currentToken() == Core.SHARE:
                self.printToken(self.scanner.currentToken().name.lower()+" ")
                self.scanner.nextToken()
                if self.scanner.currentToken() == Core.ID:
                    self.printToken(self.scanner.getID())
                    self.scanner.nextToken()
                    if self.scanner.currentToken() == Core.SEMICOLON:
                        self.printToken(";\n")
                        self.scanner.nextToken()
                    else:
                        print("ERROR: Expecting Semicolon token, received " + self.scanner.currentToken().name.lower())
                        exit(0)
                else:
                    print("ERROR: Expecting ID token, received " + self.scanner.currentToken().name.lower())
                    exit(0)
            else:
                new = Expr(self.scanner)
                new.parse()
                if self.scanner.currentToken() == Core.SEMICOLON:
                    self.printToken(";\n")
                    self.scanner.nextToken()
                else:
                    print("ERROR: Expecting Semicolon token, received " + self.scanner.currentToken().name.lower())
                    exit(0)
        else:
            print("ERROR: Expecting Assign, received "+self.scanner.currentToken().name.lower())
            exit(0)

    def printToken(self, token):
        print(token, end="")
        