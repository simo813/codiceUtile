#da lab 14
import networkx as nx

from model.model import Model

model = Model()
model.createGraph(2, 5)
graph = model.graphMO
print("Num nodi:", graph.number_of_nodes())
print("Num archi:", graph.number_of_edges())
path = model.getLongestPathFrom(10)
print("Path:", path)
maxPath, maxPathWeight = model.getMaxPath()
print("MaxPath:", maxPath)
print("MaxPathWeight:", maxPathWeight)

