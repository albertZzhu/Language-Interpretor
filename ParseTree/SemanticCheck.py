

class SemanticCheck:

    def __init__(self):
        self.idList = []
        self.refList = []

    def newID(self, new):
        self.idList.append(new)

    def newREF(self, new):
        self.refList.append(new)

    def joinID(self, newList):
        self.idList.extend(newList)

    def joinREF(self, newList):
        self.refList.extend(newList)

    def ifIDExist(self, ID):
        for i in self.idList:
            if i == ID:
                return True
        return False

    def ifREFExist(self, REF):
        for i in self.refList:
            if i == REF:
                return True
        return False
