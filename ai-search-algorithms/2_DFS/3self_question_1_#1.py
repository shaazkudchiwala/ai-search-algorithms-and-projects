# DFS Problem 1: Social Media Profile Search (Stop at Goal)

# Problem Statement
# You are browsing a social media platform.
# Each user’s profile lists links to their friends’ profiles.
# You want to simulate a DFS traversal of the network, 
# starting from a given user, and stop once you find a goal profile.



# Given Directed Graph
social_graph = {
    'Alice': ['Bob', 'Claire'],
    'Bob': ['Diana', 'Eve'],
    'Claire': ['Frank'],
    'Diana': ['Gina'],
    'Eve': [],
    'Frank': ['Helen'],
    'Gina': [],
    'Helen': []
}


def dfs_social_search(graph, starting_profile, goal_profile):
    visited = {starting_profile}
    stack = [starting_profile]

    while stack:
        current_profile = stack.pop()
        print(current_profile, end=" ")

        if current_profile == goal_profile:
            print(f"\nGoal Found: {goal_profile}")
            return
            

        for friend_profile in reversed(graph[current_profile]):
            if friend_profile not in visited:
                visited.add(friend_profile)
                stack.append(friend_profile)

    print("\nGoal not found!")    #DFS doen't guarantee finding the goal node.



dfs_social_search(social_graph, 'Alice', 'Helen')   #Goal found

# dfs_social_search(social_graph, 'Alice', 'A')     #Goal not found