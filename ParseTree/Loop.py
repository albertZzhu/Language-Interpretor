from Core import Core
from Scanner import Scanner
from .Cond import Cond


class Loop:

    def __init__(self, scanner, numIndent):
        self.scanner = scanner
        self.numIndent = numIndent

    def parse(self):
        from .Stmt_seq import Stmt_seq
        if self.scanner.currentToken() == Core.WHILE:
            self.printToken("\t" * self.numIndent+self.scanner.currentToken().name.lower())
            self.scanner.nextToken()
            new = Cond(self.scanner)
            new.parse()
            if self.scanner.currentToken() == Core.BEGIN:
                self.printToken(" "+self.scanner.currentToken().name.lower()+"\n")
                self.scanner.nextToken()
                new = Stmt_seq(self.scanner, self.numIndent+1)
                new.parse()
                if self.scanner.currentToken() == Core.ENDWHILE:
                    self.printToken("\t" * self.numIndent+self.scanner.currentToken().name.lower()+"\n")
                    self.scanner.nextToken()
                else:
                    print("ERROR: ENDWHILE token expected, received" + self.scanner.currentToken().name)
                    exit(0)
            else:
                print("ERROR: BEGIN token expected, received" + self.scanner.currentToken().name)
                exit(0)
        else:
            print("ERROR: WHILE token expected, received" + self.scanner.currentToken().name)
            exit(0)

    def printToken(self, token):
        print(token+" ", end="")
