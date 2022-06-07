# Python program to print connected
# components in an undirected graph


class connectedComp:

    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def DFSUtil(self, temp, v, visited):
        visited[v] = True
        temp.append(v)
        for i in self.adj[v]:
            if not visited[i]:
                temp = self.DFSUtil(temp, i, visited)
        return temp

    def addEdge4Components(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(0, self.V):
            visited.append(False)
        for v in range(0, self.V):
            if not visited[v]:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        cc.pop(0)
        return cc

    def sumWeigth(self, cc, values):
        components = []
        for component in cc:
            suma_componente = 0
            for elemento in component:
                if(values[elemento] != 9000000000):
                    suma_componente += values[elemento]
            components.append(suma_componente)
        return components

