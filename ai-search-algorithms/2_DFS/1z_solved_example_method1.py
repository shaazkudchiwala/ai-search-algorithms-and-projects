# Using my own Logic. 
# Gives the correct output, but not preffered for DFS.
# May fail for more complex graphs (not confirmed tho).

# More time required (O(n^2)), more space, simple but least efficient.



graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}


def dfs(graph, starting_node):
    visited = []
    # visited = [starting_node]
    stack = [starting_node]

    while stack:
        node = stack.pop(0)
        print(node, end=" ")

        for linking_node in graph[node]:
            if linking_node not in visited:
                temp_list = list(graph[node])
                stack = temp_list + stack
                visited = visited + temp_list



dfs(graph, '5')
