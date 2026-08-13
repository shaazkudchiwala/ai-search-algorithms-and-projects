# Lab Exercise Solution Code:

def bfs(graph, starting_node):
    visited.append(starting_node)
    queue.append(starting_node)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        #adding children (of popped element) to the queue (FIFO)
        for linking_node in graph[node] :
            if linking_node not in visited: #condition to prevent infinite execution
                queue.append(linking_node)
                visited.append(linking_node)


graph = {
    'P' : ['S', 'R', 'Q'],
    'Q' : ['P', 'R'],
    'R' : ['P', 'Q', 'T'],
    'S' : ['P'],
    'T' : ['R']
}

visited = []
queue = []

print("BFS:")
bfs(graph, 'P')