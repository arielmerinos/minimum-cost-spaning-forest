import sys

from datastructures.Graph import Graph
from utlis import handleTXT

def run():
    header, lines = handleTXT.readTxt(sys.argv[1])
    graph = Graph(max(header) + 1)
    for arista in lines:
        graph.add_edge(arista[0], arista[1], arista[2])
    graph.Prim()

if __name__ == '__main__':
    run()
