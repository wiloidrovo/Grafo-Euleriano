# Definition of a depth-first search function that visits nodes in the graph and returns the path of visited nodes
def dfs(u, graph, visited_edge, path=[]):
    # Iterate through the adjacent nodes of the current node u (sorted in ascending order)
    for v in sorted(graph[u]):
        # Verify if the edge (u, v) has not been visited yet
        if visited_edge[u][v] == False:
            # Define the edge (u, v) and its reverse (v, u) as visited (true)
            visited_edge[u][v], visited_edge[v][u] = True, True
            # Call the recursive DFS function with v as the new starting node and update the path
            path = dfs(v, graph, visited_edge, path)
    # After visiting all adjacent nodes, add the current node u to the path
    path = path + [u]
    # Return the updated path
    return path

# Define the check_circuit_or_path function to check if the graph has an Eulerian circuit or path
def check_circuit_or_path(graph, max_node):
    # Initialize variables to keep track of the number of nodes with odd degrees and the first odd node found
    odd_degree_nodes = 0
    odd_node = -1
    # Iterate through all nodes from 1 to max_node (inclusive)
    for i in range(max_node + 1):
        # Check if the current node i exists in the graph
        if i not in graph.keys():
            # If the node is not present in the graph, continue to the next node
            continue
        # Check if the current node has an odd degree (odd number of adjacent edges)
        if len(graph[i]) % 2 != 0:
            # Increment the count of nodes with odd degrees
            odd_degree_nodes += 1
            # Update the odd_node variable to the current node i (the first odd node found)
            odd_node = i
    if odd_degree_nodes == 0:
        # If there are no nodes with odd degrees, return (1, -1) indicating an Eulerian circuit with no odd node
        return 1, odd_node
    if odd_degree_nodes == 2:
        # If there are two nodes, return (2, odd_node) indicating an Eulerian path with the odd_node as the starting node
        return 2, odd_node
    else:
        # If there are more than two nodes, return (3, odd_node)
        return 3, odd_node
    
# Define the check_euler function to check if the graph has an Eulerian circuit or path and print the path if it exists
def check_euler(graph, max_node):
    # Call check_circuit_or_path function to determine the type of Eulerian structure and the starting node
    check, odd_node = check_circuit_or_path(graph, max_node)
    # In case 3 was returned, the example graph has no circuit nor path
    if check == 3:
        print("El grafo no tiene ni camino ni circuito Euleriano")
        return
    start_node = 1
    # In case 2 was returned, the example graph has Eulerian path
    if check == 2:
        print("El grafo tiene un camino Euleriano")
        start_node = odd_node
    # In case 1 was returned, the example graph has Eulerian circuit
    if check == 1:
        print("El grafo tiene un circuito Euleriano")

    # Initialize a matrix to keep track of visited edges
    visited_edge = [[False for _ in range(max_node + 1)] for _ in range(max_node + 1)]
    # Call the dfs function to find the circuit/path starting from the determined start_node
    path = dfs(start_node, graph, visited_edge)
    # Print the path found by the dfs function
    print(path)

# Define the main function to demonstrate the code with two example graphs (graphs must be conected)
def main():
    # Example graph G1
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
    # Example graph G2
    G2 = {
        1: [2, 3, 7],
        2: [1, 3, 5, 8],
        3: [1, 2, 4, 5],
        4: [3, 6, 7],
        5: [2, 3, 6, 8],
        6: [4, 5, 7, 8],
        7: [1, 4, 6, 8],
        8: [2, 5, 6, 7]
    }

    # Test the check_euler function with the example graphs
    check_euler(G1, 10) # Example graph G1
    check_euler(G2, 8)  # Example graph G2

# Run the main function
if __name__ == "__main__":
    main()