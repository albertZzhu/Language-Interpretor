from Core import Core

class Formals:

    def __init__(self, scanner, numIndent, check):
        self.scanner = scanner
        self.numIndent = numIndent
        self.check = check
        self.formals = None
        self.ID = None
        self.IDList = []

    def parse(self):
        if self.scanner.currentToken() == Core.ID:
            self.ID = self.scanner.getID()
            self.IDList.append(self.ID)
            self.check.newREF(self.ID)
            self.scanner.nextToken()
            if self.scanner.currentToken() == Core.COMMA:
                self.scanner.nextToken()
                self.formals = Formals(self.scanner, self.numIndent, self.check)
                self.IDList.extend(self.formals.parse())
        else:
            print("\nERROR: wrong Formals format, it is not a ID.")
            exit(0)
        return self.IDList

    def execute(self):
        return self.IDList

