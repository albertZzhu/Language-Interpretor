from Core import Core
from Scanner import Scanner

class Assign:

    def __init__(self, scanner, numIndent):
        self.scanner = scanner
        self.numIndent = numIndent

    def parse(self):
        