<<<<<<< HEAD
import networkx as nx
import numpy
import matplotlib.pyplot as plt
from ProteinController import ProteinController
from FileController import FileController

class GraphController:

    def __init__(self, proteins):
        self.matrix = [[]]
        for i in range(len(proteins)):
            self.matrix.insert(i, proteins[i].getDiferences())
    def getMatrix(self):
        return self.matrix

    pass
proteinController = ProteinController()
fileController = FileController()
list = fileController.parseFile(".idea\Proteins")
list = proteinController.difProteins(list)
graphController = GraphController(list)
N = numpy.matrix(graphController.getMatrix())
G = nx.from_numpy_matrix(N)
nx.draw(G)
=======
import networkx as nx
import numpy
import matplotlib.pyplot as plt
from ProteinController import ProteinController
from FileController import FileController

class GraphController:

    def __init__(self, proteins):
        self.matrix = [[]]
        for i in range(len(proteins)):
            self.matrix.insert(i, proteins[i].getDiferences())
    def getMatrix(self):
        return self.matrix

    pass
proteinController = ProteinController()
fileController = FileController()
list = fileController.parseFile(".idea\Proteins")
list = proteinController.difProteins(list)
graphController = GraphController(list)
N = numpy.matrix(graphController)
G = nx.from_numpy_matrix(N)
nx.draw(G)
plt.show()