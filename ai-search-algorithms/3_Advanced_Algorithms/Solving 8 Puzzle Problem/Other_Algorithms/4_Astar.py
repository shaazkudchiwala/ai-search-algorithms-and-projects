# Branch and Bound (general idea)
#  ├── Uniform Cost Search (g only)
#  ├── Greedy Best-First (h only)
#  ├── A* (g+h)
#  ├── IDA* (A* variant)
#  └── Others (for optimization problems like Knapsack, TSP, etc.)


# Explanation in simple words:

# Dijkstra:
# Explores nodes in increasing order of cost. No heuristic, just brute-force shortest path. Reliable, but slower than A* if a good heuristic exists.

# A*:
# Smart version of Dijkstra — adds h(n) (future guess) to speed things up. Finds the shortest path much faster in practice, but memory-hungry.

# IDA*:
# Same optimality as A*, but fixes the memory issue. Instead of keeping all nodes, it does repeated DFS with a cost cutoff. Slower than A* but survives where A* runs out of memory.


# 📌 Real World Choices:
# Navigation apps (Google Maps, GPS routing): A* with heuristics (straight-line distance).
# Blockchain / AI agent pathfinding (large search spaces): IDA* when memory is a bottleneck.
# Basic graph routing, shortest distance (networking): Dijkstra.


# ⚡ Shaaz, here’s the cheat takeaway:
# If memory isn’t an issue → A* is the king.
# If memory is tight (like puzzles, robotics) → IDA* is the savior.
# If no heuristic exists (or graph is weighted but no geometry) → Dijkstra is the fallback.


# - - - - - - - 

# A* Algorithm: f(n) = g(n) + h(n)

# h(n) means heuristic function applied to a node n.
# It estimates the cost from the current node n to the goal.

# h(n) can be M1: No. of misplaced tiles (number of tiles that are not in their goal position except 0 tile) 
# OR M2: Manhattan Distance (slower but more accurate): ∑(distance each tile is from its goal position​)

# g(n) = cost so far → the path cost from the start state to the current state n = here, self.moves
# f(n) = total estimated cost of solution passing through node n.

#Using Manhattan Distance:


import heapq
from itertools import count

class PuzzleState:
    def __init__(self, board, empty_pos, moves=0, parent=None):
        # store board as immutable tuple-of-tuples once
        # allow passing either a list-of-lists or already a tuple-of-tuples
        if not isinstance(board, tuple):
            self.board = tuple(tuple(row) for row in board)
        else:
            self.board = board

        self.empty_pos = empty_pos
        self.moves = moves
        self.parent = parent
        self.cost = 0  # f = g + h

    def __repr__(self):
        return "\n".join(" ".join(str(x) for x in row) for row in self.board)

    def __eq__(self, other):
        return isinstance(other, PuzzleState) and self.board == other.board

    def __hash__(self):
        return hash(self.board)

    def manhattan_distance(self, goal_positions):
        # goal_positions: dict mapping tile_value -> (row, col)
        dist = 0
        for i, row in enumerate(self.board):
            for j, val in enumerate(row):
                if val != 0:
                    gi, gj = goal_positions[val]
                    dist += abs(i - gi) + abs(j - gj)
        return dist

    def calculate_cost(self, goal_positions):
        # f = g + h
        self.cost = self.moves + self.manhattan_distance(goal_positions)

    def get_neighbors(self):
        """Generate neighbor PuzzleState objects (no deepcopy)."""
        neighbors = []
        x, y = self.empty_pos
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:  # up, down, left, right
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                # make a quick 2D mutable copy (row slices), swap, then freeze to tuple-of-tuples
                rows = [list(r) for r in self.board]   # shallow copy rows (fast)
                rows[x][y], rows[nx][ny] = rows[nx][ny], rows[x][y]
                new_board = tuple(tuple(r) for r in rows)
                neighbors.append(PuzzleState(new_board, (nx, ny), self.moves + 1, self))
        return neighbors


def reconstruct_path(state):
    path = []
    while state:
        path.append(state)
        state = state.parent
    return list(reversed(path))


def solve(initial, empty_tile_posi, final):
    # Normalize boards to tuple-of-tuples
    initial_board = tuple(tuple(row) for row in initial)
    final_board = tuple(tuple(row) for row in final)

    # Precompute goal positions for Manhattan distance
    goal_positions = {}
    for i, row in enumerate(final_board):
        for j, val in enumerate(row):
            goal_positions[val] = (i, j)

    initial_state = PuzzleState(initial_board, tuple(empty_tile_posi))
    initial_state.calculate_cost(goal_positions)

    pq = []
    tie = count()
    heapq.heappush(pq, (initial_state.cost, next(tie), initial_state))

    visited = set()           # store boards (tuple-of-tuples) that are closed
    nodes_expanded = 0

    while pq:
        _, _, state = heapq.heappop(pq)
        # use immutable board directly as key
        if state.board in visited:
            continue
        visited.add(state.board)
        nodes_expanded += 1

        if state.board == final_board:
            path = reconstruct_path(state)
            for i, step in enumerate(path):
                print(f"Move {i}:")
                print(step)
                print()
            print("Total Moves:", state.moves)
            print("Total Nodes Expanded:", nodes_expanded)
            return

        for neighbor in state.get_neighbors():
            if neighbor.board not in visited:
                neighbor.calculate_cost(goal_positions)
                heapq.heappush(pq, (neighbor.cost, next(tie), neighbor))

    print("❌ Goal not reachable")


# ---- Example run ----
if __name__ == "__main__":
    initial = [[1, 2, 3],
               [5, 6, 0],
               [7, 8, 4]]

    final = [[1, 2, 3],
             [5, 8, 6],
             [0, 7, 4]]

    empty_tile_posi = [1, 2]

    solve(initial, empty_tile_posi, final)



# Takeaways:

# Definition:​

# Manhattan distance =∑(distance each tile is from its goal position)
# Same example:
# 5 is 1 move away, 6 is 1 away, 8 is 2 away
# So h₂(n) = 1 + 1 + 2 = 4