# Iterative Deepening Search

# Think of IDA* as a blend of DFS + A*.

# The Problem:
# A* needs too much memory (it keeps all nodes in memory: O(b^d) where b = branching factor, d = depth).
# For puzzles like 15-puzzle, memory blows up.

# The Idea of IDA*:
# Use f(n) = g(n) + h(n) like A*.

# But instead of storing all nodes, it does iterative deepening search:
# Start with a threshold = h(start).
# Run a DFS, but cut off whenever f(n) > threshold.
# If goal not found, increase threshold to the minimum f(n) that exceeded the cutoff.
# Repeat until goal is found.