# Modified Problem Statement:
# DFS Problem 2: Detecting Cycles in a Computer Network

# Problem Statement:
# Given a directed graph representing a computer network, 
# use DFS to check if there’s a cycle 
# (a path that starts and ends at the same node).

# Modification: Also print the path that is making the cycle. 
# In, fact print all the cycles forming. Eg: Cycle1: Cycle2:



# Using Itrative- Best.


# Given Graph (Directed):
network_graph = {
    'Server1': ['Server2'],
    'Server2': ['Server3'],
    'Server3': ['Server4', 'Server1'],  # creates a cycle back to Server1
    'Server4': []
}


from collections import deque

def find_cycles_iterative(graph):
    visited = set()
    cycles = []
    cycle_num = 0

    for start in graph:
        if start not in visited:
            stack = [(start, [start])]
            while stack:
                node, path = stack.pop()
                visited.add(node)

                for neighbour in graph[node]:
                    if neighbour in path:  # Found a cycle
                        cycle_num += 1
                        cycle_start_index = path.index(neighbour)
                        cycle_path = path[cycle_start_index:] + [neighbour]
                        cycles.append(f"Cycle{cycle_num}: {' -> '.join(cycle_path)}")
                    elif neighbour not in visited:
                        stack.append((neighbour, path + [neighbour]))

    if cycles:
        for cycle in cycles:
            print(cycle)
    else:
        print("No cycles found.")


# Test
network_graph = {
    'Server1': ['Server2'],
    'Server2': ['Server3'],
    'Server3': ['Server4', 'Server1'],  # creates a cycle back to Server1
    'Server4': []
}

find_cycles_iterative(network_graph)
