# Solved Example Solution Code:

def bfs(visited, graph, node):
    visited.append(node)    #optional line
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

graph = {
    5: [3, 7],
    3: [2, 4],
    7: [8],
    2: [],
    4: [8],
    8: []
}


visited = []
queue = []

print("BFS:")
bfs(visited, graph, 5)
