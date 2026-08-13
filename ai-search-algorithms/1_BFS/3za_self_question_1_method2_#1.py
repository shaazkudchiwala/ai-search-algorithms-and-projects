# You’re crawling a website starting from 
# the 'Home' page. Use Breadth-First Search (BFS) 
# to traverse the entire website structure.


#Iterative BFS


from collections import deque

def bfs(graph, starting_page):
    page_list = deque([starting_page])  #Queue
    visited = {starting_page}

    while page_list:

        page = page_list.popleft()
        print(page, end=" ")

        for linking_page in graph[page]:
            # if linking_page not in visited: ##Not necessary here only because it is a directed graph and we cannot go back from where we started.
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


bfs(website_graph, 'Home')



# Note that here we're making the visited and page_list (queue) variables local. Hence a better practise.