def dfs(u, graph, visited_edge, visited_node, path=[]):
    visited_node[u] = True
    for v, num_edges in graph[u].items():
        if num_edges > 0 and not visited_edge[u][v]:
            visited_edge[u][v], visited_edge[v][u] = True, True
            path = dfs(v, graph, visited_edge, visited_node, path)
    path = path + [u]
    return path

def check_circuit_or_path(graph, max_node):
    odd_degree_nodes = 0
    odd_node = -1
    for i in range(1, max_node + 1):
        degree = sum(graph[i].values())
        if degree % 2 != 0:
            odd_degree_nodes += 1
            odd_node = i
    if odd_degree_nodes == 0:
        return 1, odd_node
    if odd_degree_nodes == 2:
        return 2, odd_node
    else:
        return 3, odd_node

def check_euler(graph, max_node):
    visited_edge = {i: {j: False for j in range(1, max_node + 1)} for i in range(1, max_node + 1)}
    visited_node = [False] * (max_node + 1)
    start_node = 1

    path = dfs(start_node, graph, visited_edge, visited_node)
    if not all(visited_node[i] for i in range(1, max_node + 1)):
        print("El grafo no es conexo.")
        return

    check, odd_node = check_circuit_or_path(graph, max_node)
    if check == 3:
        print("El grafo no tiene ni camino ni circuito Euleriano")
        return

    if check == 2:
        print("El grafo tiene un camino Euleriano")
        start_node = odd_node
    if check == 1:
        print("El grafo tiene un circuito Euleriano")
    print(path)

def main():
    G1 = {
        1: {2: 1, 6: 1, 7: 1, 8: 1},
        2: {1: 1, 3: 1},
        3: {2: 1, 4: 1, 8: 1, 9: 1},
        4: {3: 1, 5: 1, 9: 1, 10: 1},
        5: {4: 1, 6: 1},
        6: {1: 1, 5: 1, 7: 1, 10: 1},
        7: {1: 1, 6: 1, 8: 1, 10: 1},
        8: {1: 1, 3: 1, 7: 1, 9: 1},
        9: {3: 1, 4: 1, 8: 1, 10: 1},
        10: {4: 1, 6: 1, 7: 1, 9: 1}
    }

    G2 = {
        1: {2: 1, 3: 1},
        2: {1: 1, 3: 1, 4: 1, 5: 1},
        3: {1: 1, 2: 1, 4: 1, 6: 1},
        4: {2: 1, 3: 1, 5: 1, 6: 1},
        5: {2: 1, 4: 1, 6: 1, 7: 1},
        6: {3: 1, 4: 1, 5: 1, 7: 1},
        7: {5: 1, 6: 1}
    }

    G3 = {
        1: {2: 1, 4: 1},
        2: {1: 1, 3: 1},
        3: {2: 1, 4: 1},
        4: {1: 1, 3: 1},
        5: {6: 1, 7: 1},
        6: {5: 1, 7: 1},
        7: {5: 1, 6: 1}
    }

    G4 = {
        1: {2: 1, 3: 1, 7: 1},
        2: {1: 1, 3: 1, 5: 1, 8: 1},
        3: {1: 1, 2: 1, 4: 1, 5: 1},
        4: {3: 1, 6: 1, 7: 1},
                5: {2: 1, 3: 1, 6: 1, 8: 1},
        6: {4: 1, 5: 1, 7: 1, 8: 1},
        7: {1: 1, 4: 1, 6: 1, 8: 1},
        8: {2: 1, 5: 1, 6: 1, 7: 1}
    }

    G5 = {
        1: {2: 1, 4: 1},
        2: {1: 1, 3: 2, 5: 1},
        3: {2: 2, 4: 1, 5: 1},
        4: {1: 1, 3: 1},
        5: {2: 1, 3: 1, 6: 1, 7: 1},
        6: {5: 1, 7: 1},
        7: {5: 1, 6: 1}
    }

    check_euler(G1, 10)  # circuito E.
    check_euler(G2, 7)   # circuito E.
    check_euler(G3, 7)   # no conexo
    check_euler(G4, 8)   # camino E.
    check_euler(G5, 7)   # multigrafo

if __name__ == "__main__":
    main()
