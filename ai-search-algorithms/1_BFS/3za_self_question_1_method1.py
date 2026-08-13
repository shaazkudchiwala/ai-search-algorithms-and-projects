# You’re crawling a website starting from 
# the 'Home' page. Use Breadth-First Search (BFS) 
# to traverse the entire website structure.

# Using lists



def bfs(graph, starting_page):
    page_list = [starting_page]  #Queue
    visited = [starting_page]

    print("\n")

    while page_list:
        page = page_list.pop(0)
        print(page, end=" ")

        for linking_page in graph[page]:
            if linking_page not in visited:
                page_list.append(linking_page)
                visited.append(linking_page)
    
    print("\n")




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

