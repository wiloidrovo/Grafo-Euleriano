def dfs(u, graph, visited_edge, path=[]):
    #path = path + [u]
    for v in graph[u]:
        if visited_edge[u][v] == False:
            visited_edge[u][v], visited_edge[v][u] = True, True
            path = dfs(v, graph, visited_edge, path)
    path = path + [u]
    return path




"""
def dfs(u, graph, visited_edge, path=[]):
    for v in graph[u]:
        if visited_edge[u][v] == False:
            visited_edge[u][v], visited_edge[v][u] = True, True
            path = dfs(v, graph, visited_edge, path)
    path.append(u)
    return path
"""




def check_circuit_or_path(graph, max_node):
    odd_degree_nodes = 0
    odd_node = -1
    for i in range(max_node + 1):
        if i not in graph.keys():
            continue
        if len(graph[i]) % 2 != 0:
            odd_degree_nodes += 1
            odd_node = i
    if odd_degree_nodes == 0:
        return 1, odd_node
    if odd_degree_nodes == 2:
        return 2, odd_node
    else:
        return 3, odd_node

def check_euler(graph, max_node):
    #check, odd_node = check_circuit_or_path(graph, max_node) #descomentar
    visited_edge = [[False for _ in range(max_node + 1)] for _ in range(max_node + 1)] #comentar
    check, odd_node = check_circuit_or_path(graph, max_node) #comentar
    if check == 3:
        print("El grafo no tiene ni camino ni circuito Euleriano")
        return
    start_node = 1
    if check == 2:
        print("El grafo tiene un camino Euleriano")
        start_node = odd_node
    if check == 1:
        print("El grafo tiene un circuito Euleriano")
    #visited_edge = [[False for _ in range(max_node + 1)] for _ in range(max_node + 1)] #descomentar
    path = dfs(start_node, graph, visited_edge)
    print(path)

def main():

    G1 = {
        1: [2, 6, 7, 8],
        2: [1, 3],
        3: [2, 4, 8, 9],
        4: [3, 5, 9, 10],
        5: [4, 6],
        6: [1, 5, 7, 10],
        7: [1, 6, 8, 10],
        8: [1, 3, 7, 9],
        9: [3, 4, 8, 10],
        10: [4, 6, 7, 9]
    }

    G2 = {
        1: [2, 3],
        2: [1, 3, 4, 5],
        3: [1, 2, 4, 6],
        4: [2, 3, 5, 6],
        5: [2, 4, 6, 7],
        6: [3, 4, 5, 7],
        7: [5, 6]
    }
    
    G3 = {
        1: [2, 4],
        2: [1, 3],
        3: [2, 4],
        4: [1, 3],
        5: [6, 7],
        6: [5, 7],
        7: [5, 6]
    }

    G4 = {
        1: [2, 3, 7],
        2: [1, 3, 5, 8],
        3: [1, 2, 4, 5],
        4: [3, 6, 7],
        5: [2, 3, 6, 8],
        6: [4, 5, 7, 8],
        7: [1, 4, 6, 8],
        8: [2, 5, 6, 7]
    }

    check_euler(G1, 10) # circuito E.
    check_euler(G2, 7)  # circuito E.
    check_euler(G3, 7)  # no conexo
    check_euler(G4, 8)  # camino E.

if __name__ == "__main__":
    main()