# We're doing the same thing
# But this code is cleaner, faster and more efficient:

from collections import deque

def bfs(graph, starting_node):
    visited = set()              # To track visited nodes
    queue = deque([starting_node])  # Queue using deque for efficient FIFO

    while queue:
        node = queue.popleft()   # Pop from left (FIFO)
        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Sample graph
graph = {
    'P': ['S', 'R', 'Q'],
    'Q': ['P', 'R'],
    'R': ['P', 'Q', 'T'],
    'S': ['P'],
    'T': ['R']
}

print("BFS:")
bfs(graph, 'P')



# Takeaways:
# Sets are faster than lists. Set's Time: O(1)
# Unique elements and hence works best.
# A deque can be used instead of a list bcoz it is more efficient for graph transversal. Allows you to pop and append items from both left and right ends.