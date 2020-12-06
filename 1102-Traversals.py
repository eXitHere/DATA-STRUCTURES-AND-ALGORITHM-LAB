class Graph:
    def __init__(self):
        self.graph = {}

    def test(self):
        print(self.graph)

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
        for v in self.graph:
            if not visited[self.get_idx(v)]:
                queue.append(v)
                visited[self.get_idx(v)] = True
            while len(queue):
                now_ = queue.pop(0)
                print(now_, end=' ')
                for x in self.graph[now_]:
                    if not visited[self.get_idx(x)]:
                        queue.append(x)
                        #print(x, end=' ')
                        visited[self.get_idx(x)] = True
        #print(visited)

    def DFS(self):
        visited = set()
        for vertex in list(self.graph):
            #print(vertex)
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
