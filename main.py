import sys

from datastructures.Graph import Graph
from datastructures.ConnectedComponents import connectedComp
from utlis import handleTXT

def run():
    header, lines = handleTXT.readTxt(sys.argv[1])
    graph = Graph(max(header) + 1)
    for arista in lines:
        graph.add_edge(arista[0], arista[1], arista[2])

    weights = graph.Prim()
    print("-----------")
    for component in graph.connectedComponents():
        print('Vertex of the Connected component: {}, total weight of the MST: {}'.format(component, weights.pop(0)))

if __name__ == '__main__':
    run()
