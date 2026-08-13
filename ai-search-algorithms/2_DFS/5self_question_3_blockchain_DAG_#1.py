# DFS Problem for Blockchain

# Problem Statement
# In a blockchain network, blocks form a directed acyclic 
# graph (DAG) in some implementations (like IOTA, Avalanche).
# You are given a graph of blocks where edges represent 
# a “block approval” relationship.
# Use DFS to check whether a newly added block introduces 
# a cycle — if it does, reject it 
# (since blockchains must remain acyclic).
# Also print the first cycle detected.

# Using Iterative DFS



import copy
# Given Directed Graph
blockchain_graph = {
    'Block1': ['Block2', 'Block3'],
    'Block2': ['Block4'],
    'Block3': ['Block4'],
    'Block4': []
}

def detect_cycle_in_blockchain(graph, new_block=None, approvals=None):
    """
    graph       : existing blockchain DAG
    new_block   : optional new block being added
    approvals   : list of blocks it approves (edges)

    blocks      : (nodes)
    edges       : Values of dict
    Keys of dict: Blocks approving the edges

    Returns True if a cycle is detected.
    """

    
    temp_graph = copy.deepcopy(graph)   # Unless proven that new block is valid, we won't touch the real graph
    
    # Add the new block if provided
    if new_block and approvals:     #If new_block and approvals are not None:
        temp_graph[new_block] = approvals    #Tagging Key to Value to add a key-value pair to the dict

    cycles = []

    for block in temp_graph:
        stack = [(block, [block])]  #stack here is a list storing multiple tuples that contain pairs of node and current path
        while stack:
            current_block, path = stack.pop()    #Example: current_block = block, path = [block]

            for linking_block in temp_graph[current_block]:      #Note: reversed(temp_graph[current_block]) is also correct depending on what order you want your DFS to be in. 
                if linking_block in path:  # cycle found
                    cycle_start_index = path.index(linking_block)
                    cycle_path = path[cycle_start_index:] + [linking_block]     #String slicing + the block that completes the loop
                    cycles.append(" -> ".join(cycle_path))
                else:
                    stack.append((linking_block, path + [linking_block]))

    if cycles:
        print("Cycle(s) detected! Rejecting the new block.")
        for i, cycle in enumerate(cycles, 1):
            print(f"Cycle {i}: {cycle}")
            # return True   ##Returns after the first cycle is detected.
        # print(graph)
        return True   ##Doesn't return until all cycles are detected.
    else:
        print("No cycles detected. Adding New Block.... \nBlockchain graph remains a DAG.\n")
        if new_block and approvals:
            graph[new_block] = approvals
        print(graph)
        return False



print("Before adding a new block:")
detect_cycle_in_blockchain(blockchain_graph)

print("\nAdding a block that introduces a cycle:")
detect_cycle_in_blockchain(blockchain_graph, 'Block4', ['Block1'])







# Relevance for Blockchain

# Ensures that the blockchain remains a DAG (no cycles).
# Prevents double-spending attacks (if a block refers back to itself).
# Practical for protocols like IOTA, Avalanche, and even sidechains.


# https://chatgpt.com/share/687b841a-0644-8013-b8ca-23003a2f4f04


# Blockchain ko hum ek graph (jisme blocks = nodes, aur approvals = edges) ke roop me represent kar rahe hain.
# Graph directed hai → har edge ek hi direction me jaata hai (Block1 → Block2 ka matlab hai Block1 approve karta hai Block2 ko).
# Blockchain DAG (Directed Acyclic Graph) hona chahiye → yani koi cycle nahi ho sakta.
# Agar ek naya block add karne se cycle ban jaaye, toh blockchain invalid hai.


# ✅ So basically:
# The outer for ensures we test all nodes.
# The stack + path combo lets us simulate recursion iteratively.
# Popping gives us the node we’re exploring and how we reached it.

# https://chatgpt.com/share/687b841a-0644-8013-b8ca-23003a2f4f04