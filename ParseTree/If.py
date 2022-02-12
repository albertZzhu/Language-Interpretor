from Core import Core
from Scanner import Scanner
from .Cond import Cond
from .SemanticCheck import SemanticCheck


class If:

    def __init__(self, scanner, numIndent, check):
        self.scanner = scanner
        self.numIndent = numIndent
        self.check = check

    def parse(self):
        from .Stmt_seq import Stmt_seq
        if self.scanner.currentToken() == Core.IF:
            self.printToken("\t" * self.numIndent+self.scanner.currentToken().name.lower())
            self.scanner.nextToken()
            new = Cond(self.scanner, self.check)
            new.parse()
            if self.scanner.currentToken() == Core.THEN:
                self.printToken(" "+self.scanner.currentToken().name.lower()+"\n")
                self.scanner.nextToken()
                new = Stmt_seq(self.scanner, self.numIndent+1, self.check)
                new.parse()
                if self.scanner.currentToken() == Core.ENDIF:
                    self.printToken("\t" * self.numIndent+self.scanner.currentToken().name.lower()+"\n")
                    self.scanner.nextToken()
                elif self.scanner.currentToken() == Core.ELSE:
                    self.printToken("\t" * self.numIndent+self.scanner.currentToken().name.lower()+"\n")
                    self.scanner.nextToken()
                    new = Stmt_seq(self.scanner, self.numIndent+1, self.check)
                    new.parse()
                    if self.scanner.currentToken() == Core.ENDIF:
                        self.printToken("\t" * self.numIndent+self.scanner.currentToken().name.lower()+"\n")
                        self.scanner.nextToken()
                    else:
                        print("\nERROR: ELSE token expected, received" + self.scanner.currentToken().name)
                        exit(0)
                else:
                    print("\nERROR: ENDIF or ELSE token expected, received" + self.scanner.currentToken().name)
                    exit(0)
            else:
                print("\nERROR: THEN token expected, received" + self.scanner.currentToken().name)
                exit(0)
        else:
            print("\nERROR: If token expected, received" + self.scanner.currentToken().name)
            exit(0)
        self.check.stackExit()

    def printToken(self, token):
        print(token+" ", end="")