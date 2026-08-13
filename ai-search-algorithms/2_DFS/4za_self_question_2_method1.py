# DFS Problem 2: Detecting Cycles in a Computer Network

# Why this Problem?
# DFS is very useful for detecting cycles in graphs — e.g., in computer networks or blockchain transaction graphs.
# A cycle could mean an infinite loop of requests or malicious smart contract behavior.

# Problem Statement:
# Given a directed graph representing a computer network, 
# use DFS to check if there’s a cycle 
# (a path that starts and ends at the same node).


# Given Graph (Directed):
network_graph = {
    'Server1': ['Server2'],
    'Server2': ['Server3'],
    'Server3': ['Server4', 'Server1'],  # creates a cycle back to Server1
    'Server4': []
}


def has_cycle(graph):
    visited = set()
    recursion_stack = set()

    def dfs(node):
        if node not in visited:
            visited.add(node)
            recursion_stack.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited and dfs(neighbour):  #Basically means if neighbour not in visited and if dfs(neighbours) function returns true:
                    return True
                elif neighbour in recursion_stack:
                    return True
            recursion_stack.remove(node)
        return False    #This particular node is clear (no cycle found)

# Har node ke liye check karna hoga ki uski koi cycle to nahi ban rahi if we start from that node
    
    # Run DFS for all servers:
    for node in graph:
        if dfs(node):  #if dfs(node) returns True
            return True
    return False

print("Cycle Detected?" , has_cycle(network_graph))