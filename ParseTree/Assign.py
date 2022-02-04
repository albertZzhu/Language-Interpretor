from Core import Core
from Scanner import Scanner

class Assign:

    def __init__(self, scanner, numIndent):
        self.scanner = scanner
        self.numIndent = numIndent

    def parse(self):
        self.printToken("\t" * self.numIndent+self.scanner.getID())
        self.scanner.nextToken()
        if self.scanner.currentToken() == Core.ASSIGN:
            self.printToken(self.scanner.currentToken().name)
            self.scanner.nextToken()
            if self.scanner.currentToken() == Core.NEW:
                self.printToken(self.scanner.currentToken().name.lower())
                self.scanner.nextToken()
                if self.scanner.currentToken() == Core.CLASS:
                    self.printToken(self.scanner.currentToken().name.lower)
                    self.scanner.nextToken()
                    if self.scanner.currentToken() == Core.SEMICOLON:
                        self.printToken(self.scanner.currentToken().name.lower)
                        self.scanner.nextToken()
                    else:
                        print("ERROR: Expecting Semicolon token, received " + self.scanner.currentToken().name.lower())
                else:
                    print("ERROR: Expecting Class token, received " + self.scanner.currentToken().name.lower())
            elif self.scanner.currentToken() == Core.SHARE:
                self.printToken(self.scanner.currentToken().name.lower())
                self.scanner.nextToken()
                if self.scanner.currentToken() == Core.ID:
                    self.printToken(self.scanner.getID())
                    self.scanner.nextToken()
                    if self.scanner.currentToken() == Core.SEMICOLON:
                        self.printToken(self.scanner.currentToken().name.lower)
                        self.scanner.nextToken()
                    else:
                        print("ERROR: Expecting Semicolon token, received " + self.scanner.currentToken().name.lower())
                else:
                    print("ERROR: Expecting ID token, received " + self.scanner.currentToken().name.lower())
            else:
                new = Expr(self.scanner)
                new.parse()
        else:
            print("ERROR: Expecting Assign, received "+self.scanner.currentToken().name.lower())


    def printToken(self, token):
        print(token+" ", end="")
        