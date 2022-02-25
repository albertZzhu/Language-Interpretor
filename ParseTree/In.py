from Core import Core
from .SemanticCheck import SemanticCheck


class In:

    def __init__(self, scanner, numIndent, check, memory, data):
        self.scanner = scanner
        self.numIndent = numIndent
        self.check = check
        self.memory = memory
        self.data = data
        self.id =  ""

    def parse(self):
        if self.scanner.currentToken() == Core.INPUT:
            self.printToken("\t" * self.numIndent+self.scanner.currentToken().name.lower()+" ")
            self.scanner.nextToken()
            if self.scanner.currentToken() == Core.ID:
                if not (self.check.ifIDExist(self.scanner.getID()) or self.check.ifREFExist(self.scanner.getID())):
                    print("\nERROR: ID: " + self.scanner.getID() + " not declared")
                    exit(0)
                self.id = self.scanner.getID()
                self.printToken(self.scanner.getID())
                self.scanner.nextToken()
                if self.scanner.currentToken() == Core.SEMICOLON:
                    self.printToken(";\n")
                    self.scanner.nextToken()
                else:
                    print("\nERROR: SEMICOLON token expected, received" + self.scanner.currentToken().name)
                    exit(0)
            else:
                print("\nERROR: ID token expected, received" + self.scanner.currentToken().name)
                exit(0)
        else:
            print("\nERROR: INPUT token expected, received" + self.scanner.currentToken().name)
            exit(0)

    def printToken(self, token):
        print(token, end="")

    def execute(self):
        self.memory.valueAssign(self.id, self.data.getCONST())
        self.data.nextToken()
