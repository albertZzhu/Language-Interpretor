from Core import Core
from Scanner import Scanner
from .Decl_int import Decl_int
from .Decl_ref import Decl_ref
from .SemanticCheck import SemanticCheck
from .Stmt_seq import Stmt_seq
from .Formals import Formals
from .Memory import Memory

class Func_decl:

    def __init__(self, scanner, numIndent, check, memory, data):
        self.scanner = scanner
        self.numIndent = numIndent
        self.check = check
        self.memory = memory
        self.data = data
        self.ID = None
        self.formals = None
        self.stmtSeq = None

    def parse(self):
        if self.scanner.currentToken() == Core.ID:
            self.ID = self.scanner.getID()
            self.scanner.nextToken()
            if self.scanner.currentToken() == Core.LPAREN:
                self.scanner.nextToken()
                if self.scanner.currentToken() == Core.REF:
                    self.scanner.nextToken()
                    self.check.stackEntry()
                    self.formals = Formals(self.scanner, self.numIndent, self.check)
                    self.formals.parse()
                    if self.scanner.currentToken() == Core.RPAREN:
                        self.scanner.nextToken()
                        if self.scanner.currentToken() == Core.BEGIN:
                            self.scanner.nextToken()
                            self.stmtSeq = Stmt_seq(self.scanner, self.numIndent, self.check, self.memory, self.data)
                            self.stmtSeq.parse()
                            if self.scanner.currentToken() == Core.ENDFUNC:
                                self.scanner.nextToken()
                            else:
                                print("\nERROR: wrong function format, expect ENDFUNC token.")
                                exit(0)
                        else:
                            print("\nERROR: wrong function format, expect BEGIN token.")
                            exit(0)
                    else:
                        print("\nERROR: wrong function format, expect RPAREN token.")
                        exit(0)
                else:
                    print("\nERROR: wrong function format, expect REF token.")
                    exit(0)
            else:
                print("\nERROR: wrong function format, expect LPAREN token.")
                exit(0)
        else:
            print("\nERROR: wrong function format, expect ID token.")
            exit(0)

    def execute(self):
        self.memory.addFunc(self.ID, self.stmtSeq, self.formals)



