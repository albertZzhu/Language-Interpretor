from Core import Core

class In:

    def __init__(self, scanner, numIndent):
        self.scanner = scanner
        self.numIndent = numIndent

    def parse(self):
        if self.scanner.currentToken() == Core.INPUT:
            self.printToken("\t" * self.numIndent+self.scanner.currentToken().name.lower()+" ")
            self.scanner.nextToken()
            if self.scanner.currentToken() == Core.ID:
                self.printToken(self.scanner.getID())
                self.scanner.nextToken()
                if self.scanner.currentToken() == Core.SEMICOLON:
                    self.printToken(";\n")
                    self.scanner.nextToken()
                else:
                    print("ERROR: SEMICOLON token expected, received" + self.scanner.currentToken().name)
                    exit(0)
            else:
                print("ERROR: ID token expected, received" + self.scanner.currentToken().name)
                exit(0)
        else:
            print("ERROR: INPUT token expected, received" + self.scanner.currentToken().name)
            exit(0)

    def printToken(self, token):
        print(token, end="")
