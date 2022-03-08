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
            self.scanner.nextToken()
            if self.scanner.currentToken() == Core.ID:
                if not (self.check.ifIDExist(self.scanner.getID()) or self.check.ifREFExist(self.scanner.getID())):
                    print("\nERROR: ID: " + self.scanner.getID() + " not declared")
                    exit(0)
                self.id = self.scanner.getID()
                self.scanner.nextToken()
                if self.scanner.currentToken() == Core.SEMICOLON:
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
        if self.data.currentToken() != Core.EOS:
            self.memory.valueAssign(self.id, self.data.getCONST(), False)
        else:
            print("Error: input has reached the end, no input provided.")
            exit(0)
        self.data.nextToken()
