# Solved Example Solution Code:
# Cleanest, Not recommended for very large graphs
 

#  Using a Python dictionary to act as an adjacency list
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = set()  # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  # Function for DFS (Recursion)
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# Steps when you call dfs(visited, graph, '5'):
# 1) '5' is not in visited → print 5, add to visited.
# 2) Loop through neighbors of 5: ['3', '7'].
# 3) First neighbor: '3' → recursive call dfs(..., '3')



print("Following is the Depth-First Search")
dfs(visited, graph, '5')
