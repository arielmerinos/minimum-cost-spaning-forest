from collections import defaultdict
from datastructures.MinHeap import MinHeap, print_array


class Graph:

    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    def add_edge(self, src, dest, weight):
        new_node = [dest, weight]
        self.graph[src].insert(0, new_node)
        new_node = [src, weight]
        self.graph[dest].insert(0, new_node)

    def Prim(self):
        V = self.V
        key = []
        parent = []

        min_heap = MinHeap()

        for v in range(V):
            parent.append(-1)
            key.append(9e9)
            min_heap.array.append(min_heap.new_min_heap_node(v, key[v]))
            min_heap.pos.append(v)

        min_heap.pos[0] = 0
        key[0] = 0
        min_heap.decrease_key(0, key[0])

        min_heap.size = V

        while not min_heap.is_empty():
            new_heap_node = min_heap.extract_min()
            u = new_heap_node[0]

            for pCrawl in self.graph[u]:
                v = pCrawl[0]
                if min_heap.is_in_minheap(v) and pCrawl[1] < key[v]:
                    key[v] = pCrawl[1]
                    parent[v] = u
                    min_heap.decrease_key(v, key[v])

        print_array(parent, V, key)
