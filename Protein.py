class Protein:

    def __init__(self, name, protein):
        self.name = name
        self.protein = protein
        self.diferences = []

    def getDiferences(self):
        return self.diferences

    def getName(self):
        return self.name

    def getProtein(self):
        return self.protein

    def setName(self, name):
        self.name = name

    def setProtein(self, protein):
        self.protein = protein



