import sys

from datastructures.Graph import Graph
from datastructures.ConnectedComponents import connectedComp
from utlis import handleTXT

def run():
    header, lines = handleTXT.readTxt(sys.argv[1])
    graph = Graph(max(header) + 1)
    componentes = connectedComp(max(header)+1)
    for arista in lines:
        graph.add_edge(arista[0], arista[1], arista[2])
        componentes.addEdge4Components(arista[0], arista[1])
    keys = graph.Prim()
    compos = componentes.connectedComponents()
    print(compos)
    print(componentes.sumWeigth(compos, keys))

if __name__ == '__main__':
    run()
