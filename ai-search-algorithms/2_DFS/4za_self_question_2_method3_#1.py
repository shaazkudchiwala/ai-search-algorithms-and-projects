# DFS Problem 2: Detecting Cycles in a Computer Network

# Why this Problem?
# DFS is very useful for detecting cycles in graphs — e.g., in computer networks or blockchain transaction graphs.
# A cycle could mean an infinite loop of requests or malicious smart contract behavior.

# Problem Statement:
# Given a directed graph representing a computer network, 
# use DFS to check if there’s a cycle 
# (a path that starts and ends at the same node).

# Solving by my own: Using Iterative DFS instead of Recursive DFS
# Best Method:

#ON HOLD- REVISIT LATER

# Given Graph (Directed):
network_graph = {
    'Server1': ['Server2'],
    'Server2': ['Server3'],
    'Server3': ['Server4', 'Server1'],  # creates a cycle back to Server1
    'Server4': []
}


def has_cycle(graph):
    visited = set()         # All nodes that have been fully explored
    stack_nodes = set()     # Nodes currently in the DFS stack

    for start_node in graph:
        if start_node not in visited:
            stack = [(start_node, iter(graph[start_node]))]

            while stack:
                node, children = stack[-1]
                visited.add(node)
                stack_nodes.add(node)

                try:
                    child = next(children)
                    if child not in visited:
                        stack.append((child, iter(graph[child])))
                    elif child in stack_nodes:
                        return "Cycle Detected: True"
                except StopIteration:
                    stack.pop()
                    stack_nodes.remove(node)

    return "Cycle Detected: False"


print(has_cycle(network_graph))
