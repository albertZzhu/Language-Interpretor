from Core import Core
from Scanner import Scanner
from .Cond import Cond
from .Stmt_seq import Stmt_seq

class If:

    def __init__(self, scanner, numIndent):
        self.scanner = scanner
        self.numIndent = numIndent

    def parse(self):
        if self.scanner.currentToken() == Core.IF:
            self.printToken(self.scanner.currentToken().name.lower())
            self.scanner.nextToken()
            new = Cond(self.scanner)
            new.parse()
            if self.scanner.currentToken() == Core.THEN:
                self.printToken(self.scanner.currentToken().name.lower())
                self.scanner.nextToken()
                new = Stmt_seq(self.scanner)
                new.parse()
                if self.scanner.currentToken() == Core.ENDIF:
                    self.printToken(self.scanner.currentToken().name.lower())
                    self.scanner.nextToken()
                elif self.scanner.currentToken() == Core.ELSE:
                    self.printToken(self.scanner.currentToken().name.lower())
                    self.scanner.nextToken()
                    new = Stmt_seq(self.scanner)
                    new.parse()
                    if self.scanner.currentToken() == Core.ENDIF:
                        self.printToken(self.scanner.currentToken().name.lower())
                        self.scanner.nextToken()
                    else:
                        print("ERROR: ELSE token expected, received" + self.scanner.currentToken().name)
                else:
                    print("ERROR: ENDIF or ELSE token expected, received" + self.scanner.currentToken().name)
            else:
                print("ERROR: THEN token expected, received" + self.scanner.currentToken().name)
        else:
            print("ERROR: If token expected, received" + self.scanner.currentToken().name)

    def printToken(self, token):
        print(token+" ", end="")