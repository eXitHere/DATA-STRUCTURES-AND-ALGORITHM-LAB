class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        if not self.graph.get(u):
            self.graph[str(u)] = [v]
        else:
            self.graph[str(u)] = self.graph[str(u)] + [v]
        if not self.graph.get(v):
            self.graph[str(v)] = [u]
        else:
            self.graph[str(v)] = self.graph[str(v)] + [u]

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def get_idx(self, value):
        return list(self.graph.keys()).index(value)

    def BFS(self):
        visited = [False] * (len(self.graph))
        queue = []
        s = list(self.graph.keys())[0]
        queue.append(s)
        visited[self.get_idx(s)] = True
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.graph[s]:
                idx = self.get_idx(i)
                if visited[idx] == False:
                    queue.append(i)
                    visited[idx] = True

    def DFS(self):
        visited = set()
        for vertex in list(self.graph):
            if vertex not in visited:
                self.DFSUtil(vertex, visited)

    def sort(self):
        tmp = {}
        for x in sorted(self.graph):
            #print(x)
            tmp[x] = sorted(self.graph[x])
        self.graph = tmp
        #print(self.graph)


if __name__ == "__main__":
    #inp = "A B,C D,E F,A C,A D,H G".split(",")
    inp = input("Enter : ").split(",")
    graph = Graph()
    for x in inp:
        y = x.split()
        graph.addEdge(y[0], y[1])
    graph.sort()
    print("Depth First Traversals : ", end='')
    graph.DFS()
    print("\nBredth First Traversals : ", end='')
    graph.BFS()
