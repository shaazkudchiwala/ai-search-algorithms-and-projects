# You are on a social networking platform. 
# You start at Alice, and you want to find a connection 
# path to Eve. Use BFS to simulate the friend search and 
# print the BFS graph traversal 
# route (when goal node was not found) and then 
# print the shortest path from starting node to goal node.



from collections import deque

def bfs_social_network(graph, starting_friend, goal_friend):
    friend_list = deque([starting_friend])  #Queue
    discovered = {starting_friend}  #Visited
    transversal_path = deque()
    parent = {starting_friend: None}    #Dictionary to only track the parent.

    while friend_list:
        friend = friend_list.popleft()
        transversal_path.append(friend)


        if friend == goal_friend:
            break


        for friend_of_friend in graph[friend]:
            if friend_of_friend not in discovered:
                friend_list.append(friend_of_friend)
                discovered.add(friend_of_friend)
                parent[friend_of_friend] = friend   #Genius! This tracks the actual parent of a given friend
    
    # Kya baat hai!! 
    shortest_path = deque()
    current = goal_friend
    while current is not None:
        shortest_path.appendleft(current)
        current = parent.get(current)   # current = current ka parent.

    
# Refer this for better understanding: After all iterations:
#     parent = {
#     'Alice': None,
#     'Bob': 'Alice',
#     'Claire': 'Alice',
#     'Frank': 'Alice',
#     'Diana': 'Bob',
#     'Eve': 'Bob'
#     }


    print("\nBFS transversal path to goal friend:")
    print(" -> ".join(transversal_path))

    print("\nShortest path to goal friend:")
    print(" -> ".join(shortest_path))

    



# Given graph (Undirection/ Bidirectional):
social_graph = {
    'Alice': ['Bob', 'Claire', 'Frank'],
    'Bob': ['Alice', 'Diana', 'Eve'],
    'Claire': ['Alice', 'Frank'],
    'Diana': ['Bob'],
    'Eve': ['Bob'],
    'Frank': ['Alice', 'Claire']
}

bfs_social_network(social_graph, 'Alice', 'Diana')



# ChatGPT link: https://chatgpt.com/share/687b841a-0644-8013-b8ca-23003a2f4f04


# Output:
# Alice Bob Claire Frank Diana Eve
# Alice -> Bob -> Eve

