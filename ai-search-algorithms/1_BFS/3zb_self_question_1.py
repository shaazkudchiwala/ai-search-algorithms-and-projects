# You’re crawling a website starting from 
# the 'Home' page. Use Breadth-First Search (BFS) 
# to traverse the entire website structure.

# Modification: Stop as soon as you reach goal node. 
# Goal Node: Post2



from collections import deque

def bfs(graph, starting_page, goal_node):
    page_list = deque([starting_page])  #Queue
    visited = {starting_page}

    while page_list:

        page = page_list.popleft()
        print(page, end=" ")

        if page == goal_node:
            print("\nGoal Reached! Program stopped")
            return

        for linking_page in graph[page]:
            page_list.append(linking_page)
            visited.add(linking_page)


# Given Directed Graph:
website_graph = {
    'Home': ['About', 'Blog', 'Shop'],
    'About': ['Team', 'Careers'],
    'Blog': ['Post1', 'Post2'],
    'Shop': ['Products', 'Cart'],
    'Team': [],
    'Careers': [],
    'Post1': [],
    'Post2': [],
    'Products': [],
    'Cart': []
}


bfs(website_graph, 'Home', 'Post2')



# Note that here we're making the visited and page_list (queue) variables local. Hence a better practise.