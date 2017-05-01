from Protein import Protein

class FileController:

    def getFile(self):
        return self.file

    def setFile(self, file):
        self.file = file

    def parseFile(self, way):
        i = 0
        list = []
        self.setFile(open(way,"r"))
        protein = ""
        name = ""

        for line in self.getFile().readlines():
            if (line[0] == '>'):
                if (protein != ""):
                    list.insert(i, Protein(name, protein))
                    i += 1
                protein = ""
                name = line
                name = name[0:-1]
            else:
                protein += line
                protein = protein[0:-1]
        return list






