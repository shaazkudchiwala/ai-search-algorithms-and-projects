# Most suitable for DFS. Even for large graphs. 
# Iterative DFS Method.
# Clean, Efficient.
# For stack either use list or deque- both equally efficient.

# Best method to write code: Refer 3self_question_1.py
# Iteraive DFS


def dfs(graph, starting_node):
    visited = set()         # Keep track of visited nodes
    stack = [starting_node] # Use stack for DFS

    while stack:
        node = stack.pop()  # Pop last element (LIFO)
        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            # Add neighbors in reverse order:
            for neighbour in reversed(graph[node]):
                if neighbour not in visited:
                    stack.append(neighbour)



graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

dfs(graph, '5')



# # Key Takeaways:

# list:
# append() → amortized O(1)
# pop() from end → O(1) ✅
# pop(0) from front → O(n) ❌ (bad for queues)


# deque:
# append() → O(1)
# appendleft() → O(1)
# pop() from right → O(1)
# popleft() from left → O(1)

