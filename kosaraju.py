import sys
from collections import defaultdict

# Increase the recursion limit for deep recursion calls in DFS
sys.setrecursionlimit(10**8)

def read(filename):
    # Read the graph from a file and return an adjacency list representation
    with open(filename, "r") as file:
        graphlist = defaultdict(list)
        edge_count = 0  # Counter for the number of edges
        
        for line in file:
            src, dest = map(int, line.split())
            graphlist[src].append(dest)
            edge_count += 1
        
        # Print the number of edges read
        print(edge_count)
    
    return graphlist

def dfs_utils(graphlist, v, visited, stack):
    # Util function for a depth-first search, populating the stack with vertices
    visited.add(v)
    for neighbor in graphlist[v]:
        if neighbor not in visited:
            dfs_utils(graphlist, neighbor, visited, stack)
    stack.append(v)

def dfs(graphlist, component, v, visited):
    # Main DFS function, creates SCC (Strongly Connected Component)
    visited.add(v)
    component.append(v)
    for neighbor in graphlist[v]:
        if neighbor not in visited:
            dfs(graphlist, component, neighbor, visited)

def kosaraju(graphlist):
    # Implementation of Kosaraju's algorithm to find SCCs
    visited = set()
    stack = []
    
    # Fill the stack with finishing times of vertices in DFS
    for i in range(len(graphlist)):
        if i not in visited:
            dfs_utils(graphlist, i, visited, stack)
    
    # Create a transposed graph
    transposed = defaultdict(list)
    
    for node in graphlist:
        for neighbor in graphlist[node]:
            transposed[neighbor].append(node)
    
    visited.clear()  # The visited set is cleared for reuse
    scc = []  # List to hold all the strongly connected components
    
    # Process all vertices in order defined by the stack to find SCCs
    while stack:
        v = stack.pop()
        if v not in visited:
            component = []
            dfs(transposed, component, v, visited)
            scc.append(component)
    
    # Sort the strongly connected components by length in decreasing order
    scc = sorted(scc, reverse=True, key=len)
    
    # Return the sizes of the top 5 largest components
    answer = [len(component) for component in scc[0:5]] 
    return answer
