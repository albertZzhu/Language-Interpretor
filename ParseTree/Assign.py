from Core import Core
from Scanner import Scanner
from .Expr import Expr
from .SemanticCheck import SemanticCheck


class Assign:

    def __init__(self, scanner, numIndent, check):
        self.scanner = scanner
        self.numIndent = numIndent
        self.check = check

    def parse(self):
        self.printToken("\t" * self.numIndent+self.scanner.getID())
        ifid = self.check.ifIDExist(self.scanner.getID())
        ifref = self.check.ifREFExist(self.scanner.getID())
        if not ifid and not ifref:
            print("\nID or REF: " + self.scanner.getID() + " not in list")
            exit(0)
        self.scanner.nextToken()
        if self.scanner.currentToken() == Core.ASSIGN:
            self.printToken("=")
            self.scanner.nextToken()
            if self.scanner.currentToken() == Core.NEW:
                if ifref:
                    self.printToken(self.scanner.currentToken().name.lower()+" ")
                    self.scanner.nextToken()
                    if self.scanner.currentToken() == Core.CLASS:
                        self.printToken(self.scanner.currentToken().name.lower())
                        self.scanner.nextToken()
                        if self.scanner.currentToken() == Core.SEMICOLON:
                            self.printToken(";\n")
                            self.scanner.nextToken()
                        else:
                            print("\nERROR: Expecting Semicolon token, received " + self.scanner.currentToken().name.lower())
                            exit(0)
                    else:
                        print("\nERROR: Expecting Class token, received " + self.scanner.currentToken().name.lower())
                        exit(0)
                else:
                    print("\nID cannot be assigned in this form.")
                    exit(0)
            elif self.scanner.currentToken() == Core.SHARE:
                if ifref:
                    self.printToken(self.scanner.currentToken().name.lower()+" ")
                    self.scanner.nextToken()
                    if self.scanner.currentToken() == Core.ID:
                        self.printToken(self.scanner.getID())
                        self.scanner.nextToken()
                        if self.scanner.currentToken() == Core.SEMICOLON:
                            self.printToken(";\n")
                            self.scanner.nextToken()
                        else:
                            print("\nERROR: Expecting Semicolon token, received " + self.scanner.currentToken().name.lower())
                            exit(0)
                    else:
                        print("\nERROR: Expecting ID token, received " + self.scanner.currentToken().name.lower())
                        exit(0)
                else:
                    print("\nID cannot be assigned in this form.")
                    exit(0)
            else:
                new = Expr(self.scanner, self.check)
                new.parse()
                if self.scanner.currentToken() == Core.SEMICOLON:
                    self.printToken(";\n")
                    self.scanner.nextToken()
                else:
                    print("\nERROR: Expecting Semicolon token, received " + self.scanner.currentToken().name.lower())
                    exit(0)
        else:
            print("\nERROR: Expecting Assign, received "+self.scanner.currentToken().name.lower())
            exit(0)

    def printToken(self, token):
        print(token, end="")
        