from Core import Core
from .Formals import Formals

class Func_call:

    def __init__(self, scanner, numIntent, check, memory, data):
        self.scanner = scanner
        self.numIndent = numIntent
        self.check = check
        self.memory = memory
        self.data = data
        self.formals = None
        self.programId = None
        self.program = None
        self.paramList = []
        self.actualParamList = []

    def parse(self):
        if self.scanner.currentToken() == Core.BEGIN:
            self.scanner.nextToken()
            if self.scanner.currentToken() == Core.ID:
                self.programId = self.scanner.getID()
                self.scanner.nextToken()
                if self.scanner.currentToken() == Core.LPAREN:
                    self.scanner.nextToken()
                    self.formals = Formals(self.scanner, self.numIndent, self.check)
                    self.formals.parse()
                    if self.scanner.currentToken() == Core.RPAREN:
                        self.scanner.nextToken()
                        if self.scanner.currentToken() == Core.SEMICOLON:
                            self.scanner.nextToken()
                        else:
                            print("\nERROR: Expecting SEMICOLON token form, received " + self.scanner.currentToken().name)
                            exit(0)
                    else:
                        print("\nERROR: Expecting RPAREN token form, received " + self.scanner.currentToken().name)
                        exit(0)
                else:
                    print("\nERROR: Expecting LPAREN token form, received " + self.scanner.currentToken().name)
                    exit(0)
            else:
                print("\nERROR: Expecting ID token form, received " + self.scanner.currentToken().name)
                exit(0)
        else:
            print("\nERROR: Expecting BEGIN token form, received " + self.scanner.currentToken().name)
            exit(0)

    def execute(self):
        #self.memory.debugFunction()
        self.program = self.memory.getFunc(self.programId)
        self.paramList = self.formals.execute()
        self.actualParamList = self.memory.getParam(self.programId).execute()
        #print(str(self.paramList))
        #print(str(self.actualParamList))
        self.memory.newFrame()
        for i in range(len(self.actualParamList)):
            self.memory.addLocal(self.actualParamList[i], True)
            self.memory.refCopy(self.actualParamList[i], self.paramList[i])
        self.program.execute()
        #self.memory.debugFunction()
        self.memory.popStack()
        self.memory.popFrame()


