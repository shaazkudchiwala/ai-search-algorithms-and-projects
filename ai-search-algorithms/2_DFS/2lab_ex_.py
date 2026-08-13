# Recursive Code. Good for smaller graphs.

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for linking_node in graph[node]:
            dfs(visited, graph, linking_node)  #passing on the updated visited set and same graph to the inner function (itself)


# Given Undirected Graph
graph = {
    'P': ['Q', 'R', 'S'],
    'Q': ['P', 'R'],
    'R': ['P', 'Q', 'T'],
    'S': ['P'],
    'T': ['R']
}

dfs(visited, graph, 'P')



# # Verdict:
# ✅ Your code is perfectly correct and efficient for recursive DFS.
# ⚠️ Only limitation → Python recursion depth (~1000 by default).
# For very deep graphs, iterative DFS with a stack is safer.
