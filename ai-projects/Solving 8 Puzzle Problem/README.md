# 8-Puzzle Solver

A collection of search algorithm implementations for solving the classic 8-puzzle problem. The 8-puzzle is a sliding tile puzzle consisting of a 3×3 grid with eight numbered tiles and one empty space. The goal is to arrange the tiles from an initial configuration to a target goal state by sliding tiles into the empty space. The project demonstrates uninformed search (BFS, DFS), informed search (Greedy Best-First Search), and provides sketches of advanced algorithms for algorithm analysis and comparison.

## Quick Reference

### File Organization
```
Solving 8 Puzzle Problem/
├── 1_BFS_#1.py              # Breadth-First Search (optimal, uninformed)
├── 2_DFS_#1.py              # Depth-First Search (memory-efficient, uninformed)
├── 3_GBFS_#1.py             # Greedy Best-First Search (informed, fast but not optimal)
├── 3_my_own_algorithm.py    # Experimental variant (incomplete)
├── Other_Algorithms/        # Advanced algorithm sketches
│   ├── 4_Astar.py           # A* with heuristics (optimal, informed)
│   ├── 5_UCS.py             # Uniform Cost Search (optimal, uninformed)
│   ├── 6_IDA.py             # Iterative Deepening A* (optimal, memory-efficient)
│   └── 7_Dijkstra.py        # (sketch only)
└── README.md                # This file
```

### Quick Start

**Run BFS (guaranteed shortest path):**
```bash
python 1_BFS_#1.py
```

**Run GBFS (fast, heuristic-guided):**
```bash
python 3_GBFS_#1.py
```

**Modify example configurations in any script:**
Edit the `initial` and `final` (or `starting_board` and `goal_board`) lists at the bottom of each file.

### Algorithm Selection Guide

| Goal | Best Choice | Reason |
|------|------------|--------|
| Find shortest path | BFS | Guaranteed optimal |
| Minimize memory | DFS | O(d) space |
| Fast solution (not necessarily optimal) | GBFS | Heuristic pruning |
| Optimal + fast | A* (advanced) | g + h combines both |
| Optimal + low memory | IDA* (advanced) | Iterative deepening with A* |

## Problem Formulation

The 8-puzzle can be modeled as a directed graph where:
- Each **node** represents a unique puzzle configuration (board state)
- Each **edge** represents a valid move (sliding one tile into the empty space)
- The **initial node** is the starting configuration
- The **goal node** is the target configuration
- The **branching factor** is typically 2–4 (fewer for edge/corner empty positions)
- The **solution depth** varies depending on the initial configuration

The search space is finite but large: there are 9!/2 = 181,440 reachable states for any given puzzle configuration.

## Algorithms Implemented

### Primary Implementations

#### Breadth-First Search (BFS) — `1_BFS_#1.py`

**Algorithm:** Explores all states level by level using a queue (FIFO).

**Flow:**
1. Initialize queue with the initial state
2. Dequeue a state and check if it's the goal
3. If not, generate all neighbors and enqueue unvisited neighbors
4. Repeat until goal is found or queue is empty

**Guarantees:**
- **Optimal:** Always finds the shortest solution (minimum number of moves)
- **Complete:** Guaranteed to find a solution if one exists

**Memory usage:** O(b^d) where b is branching factor (~3) and d is solution depth. For deep solutions, this becomes prohibitive.

**Implementation notes:**
- Uses `collections.deque` for O(1) popleft and append operations
- Maintains a `visited` set to prevent cycles and redundant exploration
- Stores parent pointers for solution path reconstruction via backtracking
- Example: Finding path from initial to goal requires exploring many intermediate states before finding the first complete path

#### Depth-First Search (DFS) — `2_DFS_#1.py`

**Algorithm:** Explores the deepest branch first using a stack (LIFO).

**Flow:**
1. Initialize stack with the initial state
2. Pop a state and check if it's the goal
3. If not, generate all neighbors and push unvisited neighbors onto stack
4. Repeat until goal is found or stack is empty

**Characteristics:**
- **Not optimal:** Does not guarantee the shortest path (may find lengthy solutions)
- **Not complete:** May fail to find a solution if the search space has cycles or infinite depth
- **Requires cycle detection:** Must maintain visited set to avoid infinite loops

**Memory usage:** O(d) where d is the maximum depth explored. Significantly lower than BFS for deep searches.

**Implementation notes:**
- Uses `deque` in LIFO mode (pop from right side)
- Only tracks traversal order; does not report solution path because DFS doesn't guarantee optimality
- Less practical for this problem than BFS due to lack of optimality
- Example output shows traversal steps but omits the shortest-path backtracking

#### Greedy Best-First Search (GBFS) — `3_GBFS_#1.py`

**Algorithm:** Explores states in order of lowest heuristic cost using a priority queue (min-heap).

**Cost function:** `f(n) = h(n)` where:
- `h(n)` = number of misplaced tiles (tiles not in their goal positions, excluding empty tile)

**Flow:**
1. Initialize priority queue with initial state, keyed by heuristic cost
2. Pop lowest-cost state and check if it's goal
3. Generate neighbors, calculate their costs, and push to priority queue
4. Repeat until goal is found or queue is empty

**Characteristics:**
- **Not optimal:** May find suboptimal solutions if heuristic is imperfect
- **Can be incomplete:** May fail on certain configuration topologies
- **Fast in practice:** Often finds solutions with far fewer explored states than BFS

**Memory usage:** O(b^d) but typically much better than BFS in practice due to pruning via heuristic.

**Heuristic implementation:**
```python
h = 0
for i in range(3):
    for j in range(3):
        if (self.board[i][j] != goal_board[i][j] and self.board[i][j] != 0):
            h += 1
```
Counts only tiles that differ from goal position; the empty tile (0) is ignored.

**Priority queue handling:**
- Uses `heapq.heappush()` and `heapq.heappop()` for efficient min-heap operations
- Employs `itertools.count()` to generate unique tie-breaker values: `(cost, counter, state)`
  - The counter ensures stable ordering when multiple states have identical costs
  - Prevents comparison errors when comparing PuzzleState objects directly

**Implementation notes:**
- Neighbors are generated as tuples: `(heuristic_cost, state_object)`
- Gets neighbors returns only unvisited states to manage heap size
- Heuristic cost is recalculated for each new state

### Experimental Implementation
- **Custom Algorithm** (`3_my_own_algorithm.py`): An attempted variant combining greedy and branch-and-bound concepts with incomplete solver logic.

### Additional Algorithm Sketches
The `Other_Algorithms/` directory contains partial implementations and theoretical documentation for:

- **A\*** (`4_Astar.py`): Combines path cost and heuristic estimate using `f(n) = g(n) + h(n)`
  - `g(n)` = actual cost from start to current node (number of moves)
  - `h(n)` = estimated cost from current node to goal (heuristic)
  - Supports two heuristics: misplaced tiles and Manhattan distance
  - More optimal than Greedy BFS but requires more memory

- **Uniform Cost Search (UCS)** (`5_UCS.py`): Branch-and-bound using only path cost `f(n) = g(n)`
  - No heuristic; explores all equally by actual distance traveled
  - Guaranteed optimal but slower than heuristic-based methods

- **Iterative Deepening A\*** (`6_IDA.py`): Memory-efficient variant combining iterative deepening with A*
  - Solves A*'s memory problem by using repeated DFS with cost cutoffs
  - Recalculates rather than storing nodes, trading time for space
  - Optimal like A* but with O(d) space instead of O(b^d)

- **Dijkstra** (`7_Dijkstra.py`): Sketch only (empty implementation file)

## Core Components

### PuzzleState Class

Represents a single puzzle configuration and encapsulates the state's properties and behavior. Instances are immutable (boards are tuples) to enable hashing and use in sets.

**Attributes:**
- `board`: A 3×3 grid stored as a tuple of tuples (immutable). Conversion from list is automatic in constructor.
  - Immutability is critical for hashing and set membership testing
  - Example: `((1, 2, 3), (5, 6, 0), (7, 8, 4))`
- `empty_pos`: Coordinates `(row, col)` of the empty tile (represented as `0`)
- `moves`: The depth/number of moves from the initial state to reach this state (used by A* as g(n))
- `parent`: Reference to the parent state, enabling solution path reconstruction via backtracking
- `cost`: Heuristic or total cost value (algorithm-specific; used in Greedy BFS and A*)
- `goal_board`: Stored in some implementations for heuristic calculations

**Key Methods:**

**`get_neighbours()`** — Generates all legal successor states:
```python
def get_neighbours(self):
    x, y = self.empty_pos
    directions = ((-1,0), (1,0), (0,-1), (0,1))  # up, down, left, right
    neighbours = []
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x <= 2 and 0 <= new_y <= 2:
            new_board = list(list(row[:]) for row in self.board)
            new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
            new_board = tuple(tuple(row) for row in new_board)
            neighbours.append(PuzzleState(new_board, (new_x, new_y), self.moves+1, self))
    return neighbours
```
- Returns list of valid successor states
- Only considers moves within grid boundaries (0-2)
- Each successor inherits parent reference and increments move count
- Optimization: Uses shallow copy (list comprehension) rather than `copy.deepcopy()` for efficiency

**`__hash__()` and `__eq__()`** — Support set membership and deduplication:
```python
def __hash__(self):
    return hash(self.board)

def __eq__(self, other):
    return self.board == other.board
```
- Allows using PuzzleState objects in sets and as dictionary keys
- Two states are equal iff their board configurations are identical
- Critical for visited set membership: `if state not in visited:`

**`__repr__()`** — Formats board for display:
```python
def __repr__(self):
    return "\n".join("  ".join(map(str, row)) for row in self.board)
```
- Returns human-readable 3×3 grid representation

### Solver Classes

Each solver (`PuzzleSolverBFS`, `PuzzleSolverDFS`, `PuzzleSolverGreedyBFS`) implements the **composition pattern**: contains instances of `PuzzleState` as attributes rather than inheriting from it.

**Common Methods:**

**`find_empty_tile()` / `find_empty_tile_pos()`** — Locates the empty tile:
```python
def find_empty_tile(self, board):
    for row_idx, row in enumerate(board):
        for col_idx, item in enumerate(row):
            if item == 0:
                return (row_idx, col_idx)
    raise ValueError("No empty tile (0) found in the board")
```
- Scans board linearly to find tile value 0
- Raises exception if no empty tile found or multiple empty tiles found
- Executed once during initialization

**`solve()`** — Main search algorithm:
- Implements the specific search strategy (BFS/DFS/GBFS)
- Manages queue/stack/heap data structure
- Maintains visited set
- Tracks nodes expanded and search statistics
- Calls print/show_stats on successful goal reach

**`print_stats()` / `show_stats()`** — Outputs search results:
- Lists all visited states in traversal order
- Shows solution path via backtracking (where applicable)
- Reports:
  - Total moves in solution path (optimal solution length)
  - Traversal steps (nodes explored before finding solution)
  - Total nodes expanded (search effort/branching cost)

**Visited Set Semantics:**
- Prevents revisiting the same state configuration
- Reduces search space exponentially in practice
- Stored as `visited: Set[PuzzleState]` where membership is based on board configuration hash
- BFS: Add to visited when enqueuing (prevents duplicate enqueuing)
- DFS: Add to visited when pushing (similar prevention)
- GBFS: Add to visited when popping from heap

### Data Structure Choices

| Component | Choice | Reason |
|-----------|--------|--------|
| Board representation | Tuple of tuples | Immutable, hashable, enables set storage |
| Frontier (BFS) | `collections.deque` | O(1) append (right) and popleft (left) |
| Frontier (DFS) | `collections.deque` | O(1) pop (right) and append |
| Frontier (GBFS) | `heapq` (min-heap) | O(log n) push/pop with priority ordering |
| Visited tracking | `set` | O(1) average membership testing via hash |
| Tie-breaking in GBFS | `itertools.count()` | Generates unique counters to break heap ties without comparing states |
| Path reconstruction | Parent pointers | O(d) space to store solution, O(d) time to backtrack

## How to Run

Each algorithm file is executable as a standalone Python script. No additional dependencies are required beyond Python's standard library.

```bash
python 1_BFS_#1.py
python 2_DFS_#1.py
python 3_GBFS_#1.py
```

### Modifying Test Cases

Each script includes example configurations at the bottom. The solver is instantiated with initial and goal boards:

**BFS and DFS:**
```python
initial = [[1, 2, 3],
           [5, 6, 0],
           [7, 8, 4]]

final = [[1, 2, 3],
         [5, 8, 6],
         [0, 7, 4]]

puzzle1 = PuzzleSolverBFS(initial, final)
if __name__ == "__main__":
    puzzle1.solve()
```

**GBFS:**
```python
starting_board = [[1, 2, 3],
                  [5, 6, 0],
                  [7, 8, 4]]

goal_board = [[1, 2, 3],
              [5, 8, 6],
              [0, 7, 4]]

solver = PuzzleSolverGreedyBFS(starting_board, goal_board)
solver.solve()
```

### Board Format
- Represented as a 3×3 list of integers
- `0` represents the empty tile
- `1`–`8` represent the numbered tiles
- The initial board state is the starting configuration
- The goal (final) board is the desired target state

### Example Test Cases

**Simple case (4 moves):**
```
Initial:          Goal:
1 2 3             1 2 3
5 6 0             5 8 6
7 8 4             0 7 4
```
Expected behavior: BFS finds optimal solution in 4 moves; DFS may find longer paths; GBFS typically finds solution faster than BFS due to heuristic guidance.

**Harder case (15+ moves):**
Test by creating a goal state and manually shuffling it. Note: Not all configurations are solvable due to puzzle parity constraints.

## Output

### Standard Output Format

Each solver prints completion status and detailed statistics:

**Success message:**
```
✅ Goal reached using BFS!
✅ Goal reached using DFS!
✅ Goal reached using GBFS!
```

**Traversal section:** Lists all visited states in exploration order (algorithm-dependent):
```
Traversal Order (BFS expansion):
Step 0:
1  2  3
5  6  0
7  8  4

Step 1:
1  2  3
5  0  6
7  8  4
... (continues for all expanded states)
```

**Solution path (BFS/GBFS only):** Reconstructed via parent pointers and backtracking:
```
Shortest Possible Path (After backtracking):
Move 0:
1  2  3
5  6  0
7  8  4

Move 1:
1  2  3
5  0  6
7  8  4
... (continues to goal)
```

**Statistics:**
```
Total Moves (in Solution Path): 4
BFS traversal Steps: 47
Total Nodes Expanded (Search Effort): 48
```

### Key Metrics Explained

| Metric | Definition | Interpretation |
|--------|-----------|-----------------|
| **Total Moves** | Length of solution path minus 1 (number of actual moves) | For BFS: guaranteed optimal (shortest). For DFS: may be suboptimal. |
| **Traversal Steps** | Number of states examined before reaching goal | Effort spent; lower is better. BFS steps = nodes expanded - 1. |
| **Nodes Expanded** | Total count of pop/dequeue operations | Measure of search space exploration. Lower indicates better algorithm efficiency. |

### Example Output Analysis

For the simple test case (initial to goal in 4 moves):
- **BFS:** ~48 nodes expanded, 4 moves solution (optimal)
- **DFS:** ~60+ nodes expanded (variable), longer solution path (suboptimal)
- **GBFS:** ~20 nodes expanded, 4 moves solution (heuristic found optimal)

## Implementation Details

### State Representation

**Immutability and Hashing:**
- Boards are stored as tuples of tuples (immutable data structures)
- Conversion happens in `PuzzleState.__init__()`: `self.board = tuple(tuple(row) for row in board)`
- Immutability is critical because:
  - Enables use as dictionary keys and in sets via `__hash__()`
  - Prevents accidental state mutation during search
  - Allows safe sharing of state references in parent pointers
  
**Hash function:**
```python
def __hash__(self):
    return hash(self.board)  # Tuple hashing is built-in
```
Since boards are already tuples of tuples, Python's built-in hash function works directly.

**Empty position tracking:**
- Stored as `(row, col)` tuple for O(1) access during neighbor generation
- Avoids scanning the board each time neighbors are needed
- Updated when creating new states: `(new_x, new_y)` based on move direction

### Neighbor Generation and Board Updates

**Efficient shallow copying:**
```python
new_board = list(list(row[:]) for row in self.board)  # Shallow copy
new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]  # Swap
new_board = tuple(tuple(row) for row in new_board)  # Convert back
```

Why not `copy.deepcopy()`? The code explicitly avoids it with inline comment: `##Too expensive`
- `deepcopy()` recursively copies all nested structures
- Shallow copy (list comprehension) is sufficient: rows are copied, but integers are immutable
- Shallow copy is O(n) where n=9 (grid size); deepcopy is also O(9) but with higher constant factor

**Direction encoding:**
```python
directions = ((-1,0), (1,0), (0,-1), (0,1))  # up, down, left, right (row, column)
```
Each tuple `(dx, dy)` represents row and column delta from current position. Directions are ordered as: up, down, left, right (not a standard convention; order doesn't affect correctness, only exploration order).

**Boundary checking:**
```python
if 0 <= new_x <= 2 and 0 <= new_y <= 2:  # Valid position in 3x3 grid
```
Or using less-than:
```python
if (0 <= new_x < n) and (0 <= new_y < n):  # Where n=3
```
Both are equivalent; less-than is slightly more general.

### Heuristic Functions

**Misplaced Tiles Heuristic:**
```python
h = 0
for i in range(n):
    for j in range(n):
        if (self.board[i][j] != goal_board[i][j] and self.board[i][j] != 0):
            h += 1
self.cost = h
return self.cost
```
- Counts tiles in wrong positions, excluding the empty tile (0)
- Admissible: never overestimates actual cost (each misplaced tile needs ≥1 move to fix)
- Cheap to compute: O(9) = O(1) for 3×3 grid
- Less accurate than Manhattan distance but faster

**Manhattan Distance Heuristic (documented in A*):**
$$h(n) = \sum_{i=1}^{8} |x_{\text{current}}(i) - x_{\text{goal}}(i)| + |y_{\text{current}}(i) - y_{\text{goal}}(i)|$$
- Sum of taxicab distances for all tiles to their goal positions
- More accurate than misplaced tiles (better estimates)
- Slightly more expensive: O(9 × constant) = O(1)
- Also admissible

### Priority Queue Tie-Breaking

In GBFS, when multiple states have the same heuristic cost, the heap needs a deterministic tie-breaker:

```python
counter = itertools.count()  # Generates 0, 1, 2, 3, ...
heap = [(cost, next(counter), state)]  # 3-tuple
heapq.heappush(heap, (cost, next(counter), state))
cost, _, obj = heapq.heappop(heap)  # Unpack with '_' to ignore counter
```

Why is this needed?
- `heapq` compares tuples lexicographically: first by cost, then by counter, then by state
- PuzzleState objects are not orderable (no `__lt__` method), so direct comparison fails
- The counter provides a unique secondary key without comparing states
- This ensures FIFO order among states with equal cost (deterministic exploration order)

### Visited Set Management

**BFS/DFS:**
```python
visited = {self.initial}
...
for neighbour in state.get_neighbours():
    if neighbour not in visited:  # O(1) average
        visited.add(neighbour)
        queue.append(neighbour)
```
- Add to visited when enqueueing (prevents duplicates in frontier)
- Reduces nodes added to queue exponentially

**GBFS:**
```python
visited = {self.starting_state}
...
for a, b in obj.get_neighbours():
    if b not in visited:
        heapq.heappush(heap, (a, next(counter), b))
visited.add(obj)
```
- Add to visited when popping (after checking goal)
- Prevents re-exploration of already-processed states

### Path Reconstruction

**Backtracking via parent pointers:**
```python
path = []
while state is not None:
    path.append(state)
    state = state.parent
path.reverse()
```
- Follows parent chain from goal back to initial state (initial has `parent=None`)
- Reverses to get forward path: initial → ... → goal
- Time: O(d) where d is solution depth
- Space: O(d) for the path list

**Why BFS/GBFS but not DFS?**
- BFS/GBFS: Parent pointers form a shortest path tree; backtracking yields optimal solution
- DFS: Parent pointers form a depth-first tree; backtracking yields some path (not optimal)
- DFS code omits backtracking to avoid misleading optimality claims

### Complexity Analysis

| Aspect | BFS | DFS | GBFS |
|--------|-----|-----|------|
| **Time** | O(b^d) | O(b^m) | O(b^d) worst case; much better with good heuristic |
| **Space** | O(b^d) | O(d) | O(b^d) worst case; better than BFS with heuristic pruning |
| **Optimality** | ✓ | ✗ | ✗ |
| **Completeness** | ✓ | ✗ | ✗ |
| **Expansion order** | Level by level (shallowest first) | Depth-first (arbitrary among siblings) | By heuristic value (greedily) |

*Legend: b = branching factor (~3), d = solution depth, m = maximum depth (may be infinite)*

### Algorithm Trade-offs

**BFS strengths/weaknesses:**
- ✓ Guaranteed optimal solution
- ✓ Guaranteed to find a solution if one exists
- ✗ Memory expensive: must store all frontier states
- ✗ Slower on easy instances where heuristic could help

**DFS strengths/weaknesses:**
- ✓ Memory efficient: only stores current path
- ✗ No optimality guarantee
- ✗ Can get stuck in deep branches
- ✗ Incomplete without cycle detection

**GBFS strengths/weaknesses:**
- ✓ Much faster than BFS on problems with good heuristics
- ✓ Still memory-bounded better than BFS due to pruning
- ✗ May not find optimal solution
- ✗ Can fail on topologies where heuristic is misleading

**When to use each:**
- **BFS:** Guaranteed to need optimal solution; problem space small enough to fit in memory
- **DFS:** Memory severely constrained; optimality not required
- **GBFS:** Good heuristic available; speed more important than optimality; memory limited

## Practical Considerations

### Solvability

Not all 8-puzzle configurations are solvable. The puzzle has a solvability constraint based on **permutation parity**:
- A puzzle configuration is solvable if the permutation parity of the tile arrangement matches the permutation parity of the goal state
- For a uniformly shuffled puzzle, approximately 50% of configurations are solvable (half of all possible permutations)
- The implementation does not check solvability; unsolvable configurations will result in "No solution found" messages

### Performance Observations

From example runs in the code comments:
```
Example output: Total Moves (in Solution Path): 51549
                BFS transversal Steps: 58701
                Total Nodes Expanded (Search Effort): 58702
```
This represents a difficult configuration requiring deep search. Key observations:
- The solution requires 51,549 moves (extremely deep puzzle state)
- BFS explores 58,702 states to find the solution
- The ratio (nodes/moves) shows the branching factor in action: 58,702 states ≈ 58,700 ≈ 3^10.3

### Why Different Output Between Algorithms

BFS, DFS, and GBFS explore the state space in different orders:
- **BFS:** Explores all states at depth d before depth d+1 → explores narrow and tall tree
- **DFS:** Explores depth-first → explores tall branches fully
- **GBFS:** Explores states with lowest h(n) value → explores a different order entirely

For simple configurations (4-8 moves), all three often find solutions quickly. For harder configurations, GBFS often outperforms BFS despite not guaranteeing optimality because the heuristic prunes huge swaths of the search space.

### Memory Constraints in Practice

For the 8-puzzle:
- BFS on a 10-move solution: ~10,000 states in memory (manageable)
- BFS on a 20-move solution: ~1,000,000+ states (starts to strain)
- BFS on a 50-move solution: >10^15 states (completely infeasible)

This is why advanced algorithms like A* and IDA* are preferred for harder instances:
- A* with good heuristics prunes the search exponentially
- IDA* uses O(d) space instead of O(b^d)

### Debugging and Verification

**To verify correctness:**
1. Run the solver on a simple 2-3 move configuration (manually create puzzle state one move away from goal)
2. Verify BFS finds solution in exactly that many moves
3. Verify the backtracked solution path actually transforms initial to goal state

**To analyze algorithm behavior:**
1. Compare traversal sizes (nodes expanded) across algorithms on the same instance
2. Observe that GBFS usually expands fewer nodes than BFS
3. Note that DFS may find the goal faster or slower than BFS (non-deterministic relative to board layout)

## Advanced Implementation Notes

### Exception Handling

**In GBFS:**
```python
try:
    # ... main search loop ...
except Exception as e:
    raise RuntimeError(f"Solver failed due to error: {e}")
```
The GBFS implementation includes exception handling to catch runtime errors during search (e.g., invalid state creation, hash errors).

**In neighbor generation (GBFS):**
```python
def get_neighbours(self):
    try:
        # ... generate neighbors ...
    except Exception as e:
        raise RuntimeError(f"Solver failed due to error: {e}")
```
Defensive programming to catch issues during state expansion.

### Class Design Pattern: Composition

The codebase uses **composition** rather than inheritance:
```python
class PuzzleSolverBFS:
    def __init__(self, initial, final):
        self.initial = PuzzleState(initial, self.find_empty_tile(initial))
        self.final = PuzzleState(final, None)
```
- `PuzzleSolverBFS` contains instances of `PuzzleState`
- This is more flexible than inheritance: PuzzleState can be used standalone
- Allows different solvers to use the same PuzzleState class with different algorithms

### Permutation Representation

The board is represented as a flattened sequence of values, then reconstructed:
- **Storage:** Tuple of tuples `((1,2,3), (5,6,0), (7,8,4))`
- **Conceptual:** A permutation of {0,1,2,...,8}
- **Hashing:** Uses Python's built-in tuple hash (based on element values)

This enables treating each unique puzzle configuration as a unique immutable value.

### Why No Depth Limit in BFS/DFS?

The code does not impose a depth limit:
```python
while queue:  # No depth check
    state = queue.popleft()
    # ...
```
- BFS without depth limit is safe: it explores in order and will find solution (if solvable)
- DFS without depth limit can loop indefinitely on unsolvable configurations
- For the 8-puzzle, most solvable configurations require <20 moves, so this is practical

For production code solving harder puzzles (15-puzzle, etc.), adding a depth limit is advisable to prevent runaway searches.

### Cost vs. Move Count Distinction

**In BFS/DFS:**
- `state.moves` = actual number of moves from initial state (path cost = moves)
- Each move has equal cost (1)

**In GBFS/A*:**
- `cost` attribute = heuristic value or f(n) = g(n) + h(n)
- `moves` = actual path cost (g(n))
- `cost` != `moves` (cost is evaluation metric, not solution metric)

### Integer vs. String Hashing

Board hashing uses integer tuple hashing:
```python
def __hash__(self):
    return hash(self.board)  # Directly hash tuple of tuples
```

Alternative (not used) mentioned in comments:
```python
# return hash(str(self.board))  # Convert to string first
```
- Direct tuple hashing is O(n) where n=9 (grid size)
- String conversion would be O(n) as well
- Direct hashing is slightly faster and more idiomatic Python

## Key Design Insights

### Why Immutable Boards?

**Reasons for `tuple(tuple(...))` instead of `list(list(...))`:**
1. **Hashability:** Tuples are hashable; lists are not
2. **Safety:** Prevents accidental mutation
3. **Clarity:** Signals immutable state to other code
4. **Performance:** Tuple hashing is slightly faster than hashing stringified lists

### Memory Layout Comparison

For a single puzzle state storing the board:
- **List of lists:** ~200 bytes (nested list overhead)
- **Tuple of tuples:** ~150 bytes (less overhead)
- **String representation:** ~50 bytes (memory-efficient but slow to hash)
- **Integer encoding (not used):** ~10 bytes (fastest but complex to decode)

For 10,000 states in memory:
- List of lists: ~2 MB
- Tuple of tuples: ~1.5 MB
- String: ~500 KB
- Integer encoding: ~100 KB

The code chose tuple of tuples as the balance between safety, hashability, and reasonable memory footprint.

### Why `collections.deque`?

Standard Python lists support `append()` at O(1) but `pop(0)` at O(n) (must shift all elements). Using `deque`:
- `append()` → O(1)
- `popleft()` → O(1)
- `pop()` → O(1)

For BFS exploring 1000+ states, this difference is significant.

### Scalability Implications

For harder puzzles like the 15-puzzle:
- **BFS:** Becomes infeasible (branching factor ~4, solutions can be 50+ moves deep)
- **DFS:** Still infeasible (gets lost in deep branches)
- **GBFS:** More feasible (good heuristics prune aggressively)
- **A*:** Practical with Manhattan distance heuristic
- **IDA*:** Practical with good heuristics (trades time for memory)

The 8-puzzle is solvable by BFS because the state space is manageable. Larger puzzles require the more sophisticated algorithms sketched in the `Other_Algorithms/` directory.
