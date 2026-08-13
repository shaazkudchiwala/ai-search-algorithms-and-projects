# Modified Problem Statement:
# DFS Problem 2: Detecting Cycles in a Computer Network

# Problem Statement:
# Given a directed graph representing a computer network, 
# use DFS to check if there’s a cycle 
# (a path that starts and ends at the same node).

# Modification: Also print the path that is making the cycle.



# Using Recusion- Efficient but not te best.


# Given Graph (Directed):
network_graph = {
    'Server1': ['Server2'],
    'Server2': ['Server3'],
    'Server3': ['Server4', 'Server1'],  # creates a cycle back to Server1
    'Server4': []
}


def find_cycle(graph):
    visited = set()
    rec_stack = []
    
    def dfs(node):
        visited.add(node)
        rec_stack.append(node)  # push current node to path stack

        for neighbour in graph[node]:
            if neighbour not in visited:
                if dfs(neighbour):
                    return True
            elif neighbour in rec_stack:
                cycle_start_index = rec_stack.index(neighbour)
                cycle_path = rec_stack[cycle_start_index:]
                print("Cycle Path Found:", " -> ".join(cycle_path + [neighbour]))
                return True

        rec_stack.pop()  # backtrack
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False



find_cycle(network_graph)
