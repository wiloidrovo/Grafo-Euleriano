from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFSUtil(self, v, visited, path):
        visited[v] = True
        path.append(v)

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited, path)

    def isConnected(self):
        visited = [False]*(self.V)
        for i in range(self.V):
            if len(self.graph[i]) != 0:
                break

        if i == self.V-1:
            return True

        path = []
        self.DFSUtil(i, visited, path)
        for i in range(self.V):
            if visited[i] == False and len(self.graph[i]) > 0:
                return False

        return True

    def getEulerPath(self, u):
        path = []
        self.DFSUtil(u, [False]*(self.V), path)
        return path

    def getEulerCircuit(self, u):
        circuit = []
        while len(self.graph[u]) > 0:
            v = self.graph[u][0]
            self.graph[u].remove(v)
            self.graph[v].remove(u)
            circuit.extend(self.getEulerCircuit(v))
        return [u] + circuit

    def isEulerian(self):
        if self.isConnected() == False:
            return [], False

        odd = 0
        odd_vertex = None
        for i in range(self.V):
            if len(self.graph[i]) % 2 != 0:
                odd += 1
                odd_vertex = i

        if odd == 0:
            # Eulerian Circuit
            return self.getEulerCircuit(0), True
        elif odd == 2:
            # Eulerian Path
            return self.getEulerPath(odd_vertex), False
        else:
            # Not Eulerian
            return [], False

    def test(self):
        euler_path, is_circuit = self.isEulerian()
        if len(euler_path) == 0:
            print("graph is not Eulerian")
        else:
            if is_circuit:
                print("graph has an Euler circuit:")
            else:
                print("graph has an Euler path:")

            print(" -> ".join(str(node) for node in euler_path))

g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
g1.test()

g2 = Graph(5)
g2.addEdge(1, 0)
g2.addEdge(0, 2)
g2.addEdge(2, 1)
g2.addEdge(0, 3)
g2.addEdge(3, 4)
g2.addEdge(4, 0)
g2.test()

g3 = Graph(5)
g3.addEdge(1, 0)
g3.addEdge(0, 2)
g3.addEdge(2, 1)
g3.addEdge(0, 3)
g3.addEdge(3, 4)
g3.addEdge(1, 3)
g3.test()

# Let us create a graph with 3 vertices
# connected in the form of cycle
g4 = Graph(3)
g4.addEdge(0, 1)
g4.addEdge(1, 2)
g4.addEdge(2, 0)
g4.test()

# Let us create a graph with all vertices
# with zero degree
g5 = Graph(3)
g5.test()

g6 = Graph (8)
g6.addEdge(0, 1)
g6.addEdge(0, 2)
g6.addEdge(2, 1)
g6.addEdge(2, 3)
g6.addEdge(3, 4)
g6.addEdge(3, 6)
g6.addEdge(4, 5)
g6.addEdge(5, 6)
g6.addEdge(6, 7)
g6.test()

g7 = Graph (8)
g7.addEdge(0, 1)
g7.addEdge(0, 2)
g7.addEdge(2, 1)
g7.addEdge(2, 4)
g7.addEdge(1, 4)
g7.addEdge(3, 4)
g7.addEdge(3, 5)
g7.addEdge(5, 6)
g7.addEdge(6, 7)
g7.addEdge(4, 7)
g7.addEdge(4, 5)
g7.test()