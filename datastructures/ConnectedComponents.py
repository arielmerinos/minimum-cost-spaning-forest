# Python program to print connected
# components in an undirected graph


class connectedComp:

    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]



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


