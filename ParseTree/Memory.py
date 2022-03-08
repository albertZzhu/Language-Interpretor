from .SemanticCheck import SemanticCheck

class Memory:
    def __init__(self):
        self.globalList = {}
        self.stackList = [{}]
        self.heapList = []
        self.IDtracker = [[]]
        self.REFtracker = [[]]

    def addStatic(self, name, ref):
        if ref:
            self.globalList[name] = 'null'
            self.REFtracker[0].append(name)
        else:
            self.globalList[name] = 0
            self.IDtracker[0].append(name)

    def pushStack(self):
        self.stackList.append({})
        self.IDtracker.append([])
        self.REFtracker.append([])

    def popStack(self):
        self.stackList.pop()
        self.IDtracker.pop()
        self.REFtracker.pop()

    def addLocal(self, name, ref):
        if ref:
            self.stackList[len(self.stackList) - 1][name] = 'null'
            self.REFtracker[len(self.REFtracker) - 1].append(name)
        else:
            self.stackList[len(self.stackList)-1][name] = 0
            self.IDtracker[len(self.IDtracker) - 1].append(name)

    def ifIDorREF(self, name):
        opt = None
        leng = len(self.IDtracker)
        for i in range(leng - 1, -1, -1):
            for j in self.IDtracker[i]:
                if j == name:
                    opt = True
                    return opt
            for a in self.REFtracker[i]:
                if a == name:
                    opt = False
                    return opt
        return opt

    def valueAssign(self, name, value, ref):
        for i in reversed(self.stackList):
            if name in i:
                if self.ifIDorREF(name):
                    i[name] = value
                else:
                    if ref:
                        i[name] = value
                    else:
                        if i[name] == "null":
                            print("Error: reference variable has to be initialized before assign value")
                            exit(0)
                        else:
                            self.heapList[i[name]] = value
                return
        if name in self.globalList:
            if self.ifIDorREF(name):
                self.globalList[name] = value
            else:
                if ref:
                    self.globalList[name] = value
                else:
                    if self.globalList[name] == 'null':
                        print("Error: reference variable has to be initialized before assign value")
                        exit(0)
                    else:
                        self.heapList[self.globalList[name]] = value

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
                    if self.ifIDorREF(name):
                        out = i[name]
                    else:
                        out = self.heapList[i[name]]
                else:
                    print("Error: Variable not initialized.")
                    exit(0)
                return out
        if name in self.globalList:
            if self.globalList[name] != 'null':
                if self.ifIDorREF(name):
                    out = self.globalList[name]
                else:
                    out = self.heapList[self.globalList[name]]
            else:
                print("Error: Variable not initialized.")
                exit(0)
        return out

    def getActualValue(self, name):
        out = 0
        for i in reversed(self.stackList):
            if name in i:
                if i[name] != 'null':
                    out = i[name]
                else:
                    print("Error: Variable not initialized.")
                    exit(0)
                return out
        if name in self.globalList:
            if self.globalList[name] != 'null':
                out = self.globalList[name]
            else:
                print("Error: Variable not initialized.")
                exit(0)
        return out

    def debugFunction(self):
        print("Static"+str(self.globalList))
        print("Stack: "+str(self.stackList))
        print("Heap: "+str(self.heapList))






