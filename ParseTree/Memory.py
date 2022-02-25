from .SemanticCheck import SemanticCheck

class Memory:
    def __init__(self, semantic):
        self.globalList = {}
        self.stackList = [{}]
        self.heapList = []
        self.semantic = semantic

    def addStatic(self, name, ref):
        if ref:
            self.globalList[name] = 'null'
        else:
            self.globalList[name] = 0

    def pushStack(self):
        self.stackList.append({})

    def popStack(self):
        self.stackList.pop()

    def addLocal(self, name, ref):
        if ref:
            self.stackList[len(self.stackList) - 1][name] = 'null'
        else:
            self.stackList[len(self.stackList)-1][name] = 0

    def valueAssign(self, name, value):
        for i in reversed(self.stackList):
            if name in i:
                if self.semantic.ifIDExist(name):
                    i[name] = value
                else:
                    if i[name] == "null":
                        i[name] = len(self.heapList)
                        self.heapList.append(value)
                    else:
                        self.headList[i[name]]
                return
        if name in self.globalList:
            if self.semantic.ifIDExist(name):
                self.globalList[name] = value
            else:
                if self.globalList[name] == 'null':
                    self.globalList[name] = len(self.heapList)
                    self.heapList.append(value)

    def newClass(self, name):
        for i in reversed(self.stackList):
            if name in i:
                i[name] = len(self.heapList)
                self.heapList.append(0)
            return
        if name in self.globalList:
            self.globalList[name] = len(self.heapList)
            self.heapList.append(0)

    def getValue(self, name):
        out = 0
        for i in reversed(self.stackList):
            if name in i:
                if i[name] != 'null':
                    out = i[name]
                else:
                    print("Error: Variable not initialized.")
                    exit(0)
                print(name+": "+str(out))
                return out
        if name in self.globalList:
            if self.globalList[name] != 'null':
                out = self.globalList[name]
            else:
                print("Error: Variable not initialized.")
                exit(0)
        return out






