# DFS Problem 2: Detecting Cycles in a Computer Network

# Why this Problem?
# DFS is very useful for detecting cycles in graphs — e.g., in computer networks or blockchain transaction graphs.
# A cycle could mean an infinite loop of requests or malicious smart contract behavior.

# Problem Statement:
# Given a directed graph representing a computer network, 
# use DFS to check if there’s a cycle 
# (a path that starts and ends at the same node).

# Solving by my own: Using Iterative DFS instead of Recursive DFS
# 100% Correct- But low efficiecy due high time.



# Given Graph (Directed):
network_graph = {
    'Server1': ['Server2'],
    'Server2': ['Server3'],
    'Server3': ['Server4', 'Server1'],  # creates a cycle back to Server1
    'Server4': []
}


def has_cycle(graph):

    has_cycle = False
    node_path = set()

    
    def iterative_dfs_for_cycle(node):
        
        visited = {node}
        stack = [node]

        while stack:
            popped_node = stack.pop()
            # print(popped_node, end=" ")


            for linking_node in reversed(graph[popped_node]):
                if linking_node == node:
                    return True
                elif linking_node not in visited:
                    visited.add(linking_node)
                    stack.append(linking_node)
        
        return False



    for node in graph:
        if node not in node_path:
            node_path.add(node)
            if iterative_dfs_for_cycle(node):
                has_cycle = True
                return(f"Cycle Detected: {has_cycle}")
                
    
    return(f"Cycle Detected: {has_cycle}")

    

print(has_cycle(network_graph))
        
        
        
        
        

# Key Takeaways:
# 🔹 DFS Cycle Detection: Recursive vs Iterative

# ✅ Recursive DFS
# Most common in teaching & theory.
# Uses the call stack to keep track of recursion depth.
# Simpler to write & understand (rec_stack is just the Python call stack).
# Limitation: Python has a default recursion depth of 1000 (can be too small for very large graphs).

# ✅ Iterative DFS
# Uses an explicit stack (list/deque) instead of recursion.
# Avoids hitting Python’s recursion limit.
# A bit more complex to manage (you must track recursion_stack manually).
# Works well for deep graphs (like large blockchain transaction DAGs).
  