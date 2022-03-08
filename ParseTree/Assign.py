from Core import Core
from .Expr import Expr


class Assign:

    def __init__(self, scanner, numIndent, check, memory):
        self.scanner = scanner
        self.numIndent = numIndent
        self.check = check
        self.status = -1
        self.variable = ""
        self.shareID = ""
        self.memory = memory
        self.expr = None

    def parse(self):
        ifid = self.check.ifIDExist(self.scanner.getID())
        ifref = self.check.ifREFExist(self.scanner.getID())
        self.variable = self.scanner.getID()
        if not ifid and not ifref:
            print("\nID or REF: " + self.scanner.getID() + " not in list")
            exit(0)
        self.scanner.nextToken()
        if self.scanner.currentToken() == Core.ASSIGN:
            self.scanner.nextToken()
            if self.scanner.currentToken() == Core.NEW:
                self.status = 0
                if ifref:
                    self.scanner.nextToken()
                    if self.scanner.currentToken() == Core.CLASS:
                        self.scanner.nextToken()
                        if self.scanner.currentToken() == Core.SEMICOLON:
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
                self.status = 1
                if ifref:
                    self.scanner.nextToken()
                    if self.scanner.currentToken() == Core.ID:
                        self.shareID = self.scanner.getID()
                        self.scanner.nextToken()
                        if self.scanner.currentToken() == Core.SEMICOLON:
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
                self.status = 2
                self.expr = Expr(self.scanner, self.check, self.memory)
                self.expr.parse()
                if self.scanner.currentToken() == Core.SEMICOLON:
                    self.scanner.nextToken()
                else:
                    print("\nERROR: Expecting Semicolon token, received " + self.scanner.currentToken().name.lower())
                    exit(0)
        else:
            print("\nERROR: Expecting Assign, received "+self.scanner.currentToken().name.lower())
            exit(0)

    def printToken(self, token):
        print(token, end="")

    def execute(self):
        if self.status == 0:
            self.memory.newClass(self.variable)
        elif self.status == 1:
            self.memory.valueAssign(self.variable, self.memory.getActualValue(self.shareID), True)
        elif self.status == 2:
            value = self.expr.execute()
            self.memory.valueAssign(self.variable, value, False)


        