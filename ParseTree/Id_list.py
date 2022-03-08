from Scanner import Scanner
from Core import Core
from .SemanticCheck import SemanticCheck


class Id_list:

    def __init__(self, scanner):
        self.scanner = scanner
        self.list = []

    def parse(self):
        if self.scanner.currentToken() == Core.ID:
            self.list.append(self.scanner.getID())
            self.scanner.nextToken()
            if self.scanner.currentToken() == Core.COMMA:
                self.scanner.nextToken()
                new = Id_list(self.scanner)
                newlist = new.parse()
                for i in self.list:
                    for j in newlist:
                        if i == j:
                            print("\nERROR: Duplicated declare of variable: " + str(i))
                            exit(0)
                self.list.extend(newlist)
            elif self.scanner.currentToken() == Core.SEMICOLON:
                self.scanner.nextToken()
            else:
                print("\nERROR: Expecting comma or semicolon, received " + self.scanner.currentToken().name)
        else:
            print("\nERROR: not an valid ID")
            exit(0)
        return self.list

    def printToken(self, token):
        print(token, end="")
