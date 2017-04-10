from Protein import Protein
from FileController import  FileController
class ProteinController:

    def compareProteins(self,protein1, protein2):
        dif = 0
        i = 0
        if (len(protein1.getProtein()) < len(protein2.getProtein())):
            min = len(protein1.getProtein())
        else:
            min = len(protein2.getProtein())
        for i in range(min-1):
            if(protein1.getProtein()[i] != protein2.getProtein()[i]):
                dif += 1
        dif += abs(len(protein1.getProtein()) - len(protein2.getProtein()))
        return dif

    def difProteins(self, proteins):
        i = g = 0
        count = len(proteins)
        for i in range(count):
            g = i + 1
            for g in range(count):
                proteins[i].getDiferences().insert(g ,self.compareProteins(proteins[i], proteins[g]))
    pass


