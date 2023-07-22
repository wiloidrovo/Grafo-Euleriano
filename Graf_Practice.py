# Python program to check if a given graph is Eulerian or not
#Complexity : O(V+E)
from collections import defaultdict

# This class represents a undirected graph using adjacency list representation
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # Default dictionary to store graph

    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # A function used by isConnected
    def DFSUtil(self, v, visited, path):
        # Mark the current node as visited
        visited[v] = True
        path.append(v)
        
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited, path)

    '''Method to check if all non-zero degree vertices are
    connected. It mainly does DFS traversal starting from
    node with non-zero degree'''
    def isConnected(self):
        # Mark all the vertices as not visited
        visited = [False]*(self.V)

        #  Find a vertex with non-zero degree
        for i in range(self.V):
            if len(self.graph[i]) != 0:
                break

        # If there are no edges in the graph, return true
        if i == self.V-1:
            return True

        # Start DFS traversal from a vertex with non-zero degree
        path = []
        self.DFSUtil(i, visited, path)

        # Check if all non-zero degree vertices are visited
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

    '''The function returns one of the following values
       0 --> If graph is not Eulerian
       1 --> If graph has an Euler path (Semi-Eulerian)
       2 --> If graph has an Euler Circuit (Eulerian)  '''
    def isEulerian(self):

        # Check if all non-zero degree vertices are connected
        if self.isConnected() == False:
            return [], False
        # Count vertices with odd degree
        odd = 0
        odd_vertex = None
        for i in range(self.V):
            if len(self.graph[i]) % 2 != 0:
                odd += 1
                odd_vertex = i
        
        '''If odd count is 2, then semi-eulerian.
            If odd count is 0, then eulerian
            If count is more than 2, then graph is not Eulerian
            Note that odd count can never be 1 for undirected graph'''
        if odd == 0:
            # Eulerian Circuit
            return self.getEulerCircuit(0), True
        elif odd == 2:
            # Eulerian Path
            return self.getEulerPath(odd_vertex), False
        else:
            # Not Eulerian
            return [], False

    # Function to run test cases
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

# Let us create and test graphs
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