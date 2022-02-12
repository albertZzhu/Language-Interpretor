
class SemanticCheck:

    def __init__(self):
        self.idList = []
        self.refList = []

    def newID(self, new):
        self.idList[len(self.idList)-1].append(new)

    def newREF(self, new):
        self.refList[len(self.refList)-1].append(new)

    def joinID(self, newList):
        self.idList[len(self.idList)-1].extend(newList)

    def joinREF(self, newList):
        self.refList[len(self.refList)-1].append(newList)

    def stackEntry(self):
        self.idList.append([])
        self.refList.append([])

    def stackExit(self):
        if len(self.idList) != 0 and len(self.refList) != 0:
            self.idList.pop()
            self.refList.pop()

    def ifIDExist(self, ID):
        for i in self.idList:
            for j in i:
                if ID == j:
                    return True
        return False

    def ifIDDuplicate(self, ID):
        for i in self.idList[len(self.idList)-1]:
            if i == ID:
                return True
        return False

    def ifREFExist(self, REF):
        for i in self.refList:
            for j in i:
                if REF == j:
                    return True
        return False

    def ifREFDuplicate(self, REF):
        for i in self.refList[len(self.refList)-1]:
            if i == REF:
                return True
        return False

    def outputREF(self):
        for i in self.refList:
            for j in i:
                print(j, end="")

    def outputID(self):
        for i in self.idList:
            for j in i:
                print(j, end="")
