# AI Search Algorithms

A comprehensive study of graph search and state-space algorithms, progressing from fundamental graph traversal techniques to advanced problem-solving strategies. This project demonstrates uninformed search (BFS, DFS) and informed search (Greedy Best-First Search, A*) through both basic graph examples and complex applications like the 8-puzzle problem.

## Project Structure

```
ai-search-algorithms/
├── 1_BFS/                          # Breadth-First Search fundamentals
├── 2_DFS/                          # Depth-First Search fundamentals
├── 3_Advanced_Algorithms/          # Complex applications and advanced algorithms
│   └── Solving 8 Puzzle Problem/   # Complete 8-puzzle solver with multiple algorithms
└── README.md                       # This file
```

## Core Concepts

### Search Algorithms Covered

**Uninformed (Blind) Search:**
- **BFS (Breadth-First Search):** Explores nodes level-by-level using a queue. Guarantees shortest path but requires significant memory.
- **DFS (Depth-First Search):** Explores nodes depth-first using a stack or recursion. Memory-efficient but does not guarantee optimal solutions.

**Informed (Heuristic) Search:**
- **Greedy Best-First Search:** Uses heuristics to guide exploration toward the goal, reducing search space at the cost of optimality.
- **A\*:** Combines actual path cost with heuristic estimates to find optimal solutions faster than uninformed search.
- **IDA\*, UCS, Dijkstra:** Advanced variants discussed in theoretical sketches.

### Key Principles

1. **State Space Representation:** Problems are modeled as graphs where nodes are states and edges are actions.
2. **Frontier Management:** Different data structures (queues, stacks, heaps) determine exploration order.
3. **Visited Tracking:** Preventing cycles and redundant exploration is critical for efficiency.
4. **Heuristic Design:** Good heuristics dramatically improve search performance without sacrificing correctness.

## Directory Overview

### 1_BFS/ — Breadth-First Search Basics

Contains foundational BFS implementations on simple graphs. Files demonstrate:
- Basic graph representation using adjacency lists
- Queue-based level-by-level exploration
- Iterative BFS implementations
- Worked examples and self-practice exercises

**Key Files:**
- `1solved_example.py` — Simple BFS on a small graph
- `2lab_ex.py` — Lab exercise
- `3za_self_question_*_method*.py` — Multiple solution approaches to the same problem
- `4self_question_2_#1.py` — Additional practice

**Learning Focus:** Understanding how BFS explores a graph systematically; why level-by-level exploration guarantees shortest paths.

### 2_DFS/ — Depth-First Search Basics

Contains foundational DFS implementations on simple graphs. Files demonstrate:
- Recursive and iterative DFS variants
- Depth-first traversal patterns
- Stack-based exploration
- Visual representations (flowcharts, diagrams)

**Key Files:**
- `1solved_example.py` — Simple recursive DFS
- `1z_solved_example_method*.py` — Alternative implementations
- `2lab_ex_.py` — Lab exercise
- `3self_question_1_#1.py` — Practice problems
- `4za_self_question_2_method*.py` — Multiple approaches to graph problems
- `4zb_self_question_2_method*.py` — Alternative solutions
- `4z_self_question_2_Flowchart.png` — Visual flowchart
- `5self_question_3_blockchain_DAG_#1.py` — Application to blockchain structures
- `5self_question_3.jpeg` — Visual aid

**Learning Focus:** Understanding depth-first traversal; recognizing when DFS is appropriate; identifying the limitations of uninformed search.

### 3_Advanced_Algorithms/ — Complex Problems and Advanced Methods

#### Solving 8 Puzzle Problem

A complete implementation of the classic 8-puzzle problem using multiple search algorithms. The 8-puzzle demonstrates how search algorithms scale from simple graphs to complex state spaces.

**Algorithms Implemented:**
- **BFS** (`1_BFS_#1.py`) — Guarantees optimal solution; explores systematically
- **DFS** (`2_DFS_#1.py`) — Memory-efficient; does not guarantee optimality
- **Greedy Best-First Search** (`3_GBFS_#1.py`) — Fast heuristic-guided search; may sacrifice optimality
- **Custom Algorithm** (`3_my_own_algorithm.py`) — Experimental variant (incomplete)

**Advanced Sketches** (`Other_Algorithms/`):
- **A\*** (`4_Astar.py`) — Optimal informed search combining actual cost and heuristic
- **Uniform Cost Search** (`5_UCS.py`) — Explores by actual cost only
- **Iterative Deepening A\*** (`6_IDA.py`) — Memory-efficient optimal search
- **Dijkstra** (`7_Dijkstra.py`) — Shortest path baseline

**Problem Details:**
- 3×3 grid with 8 numbered tiles and one empty space
- Goal: arrange tiles from initial configuration to target configuration
- Moves: slide tiles into the empty space (up, down, left, right)
- State space: 181,440 reachable configurations (9!/2)
- Application: demonstrates how algorithms scale to larger search spaces

**Key Insights:**
- BFS becomes impractical for deep solutions (memory exponential in depth)
- Heuristic-guided search (GBFS, A*) can solve problems 100× faster
- Trade-offs between optimality, memory, and speed are fundamental to algorithm choice

**For detailed information, see [3_Advanced_Algorithms/Solving 8 Puzzle Problem/README.md](3_Advanced_Algorithms/Solving%208%20Puzzle%20Problem/README.md)**

## Algorithm Comparison at a Glance

| Algorithm | Optimal | Complete | Memory | Speed | Best For |
|-----------|---------|----------|--------|-------|----------|
| **BFS** | ✓ | ✓ | O(b^d) | Moderate | Small problems requiring guaranteed shortest path |
| **DFS** | ✗ | ✗ | O(d) | Variable | Memory-constrained scenarios; optimality not required |
| **Greedy BFS** | ✗ | ✗ | O(b^d) | Fast | Speed important; good heuristics available; optimality not critical |
| **A\*** | ✓ | ✓ | O(b^d) | Fast | Optimal solutions with heuristic guidance |
| **IDA\*** | ✓ | ✓ | O(d) | Slower | Optimal solutions with minimal memory |

*Legend: b = branching factor, d = solution depth*

## How to Use This Repository

### For Learning Basics

1. Start with **1_BFS/** to understand level-by-level exploration
   ```bash
   cd 1_BFS
   python 1solved_example.py
   python 2lab_ex.py
   ```

2. Move to **2_DFS/** to contrast depth-first exploration
   ```bash
   cd ../2_DFS
   python 1solved_example.py
   python 3self_question_1_#1.py
   ```

3. Understand the differences: BFS explores shallow, DFS explores deep

### For Advanced Applications

1. Navigate to **3_Advanced_Algorithms/Solving 8 Puzzle Problem/**
2. Read the detailed README for complete algorithm implementations
3. Run individual solvers:
   ```bash
   python 1_BFS_#1.py              # Optimal but slow on hard problems
   python 3_GBFS_#1.py             # Fast heuristic-guided search
   ```

4. Modify example configurations to test different difficulty levels
5. Compare performance metrics (nodes expanded, solution length)

### Exploration Suggestions

- **Compare algorithms on the same puzzle:** Notice how BFS explores many states before finding a solution, while GBFS reaches the goal with fewer expansions
- **Analyze heuristic impact:** The misplaced tiles heuristic guides GBFS away from dead-ends
- **Understand memory usage:** Run BFS on a difficult puzzle and observe memory constraints (vs. DFS or GBFS)
- **Study the 8-puzzle sketches:** A*, IDA*, and UCS represent the frontier of practical search algorithms

## Key Concepts Demonstrated

### State Representation
- Graphs as adjacency lists or matrices
- Puzzle boards as immutable tuples for efficient hashing
- Parent pointers for solution reconstruction

### Frontier Management
- Queues for BFS (FIFO: first-in-first-out)
- Stacks for DFS (LIFO: last-in-first-out)
- Priority heaps for informed search (min-heap by heuristic value)

### Visited Tracking
- Sets for O(1) membership testing
- Prevents revisiting states and cycles
- Enables exponential pruning of search space

### Heuristic Functions
- **Admissibility:** Heuristic never overestimates actual cost
- **Consistency:** h(n) ≤ cost(n→m) + h(m) for all successor m
- **Misplaced Tiles:** Fast, simple heuristic for puzzles
- **Manhattan Distance:** More accurate but slightly more expensive

## Running the Code

**Requirements:**
- Python 3.6+
- Standard library only (no external dependencies)

**Basic Example (BFS on a graph):**
```bash
cd 1_BFS
python 1solved_example.py
```

**Advanced Example (8-puzzle solver):**
```bash
cd 3_Advanced_Algorithms/Solving\ 8\ Puzzle\ Problem
python 1_BFS_#1.py
python 3_GBFS_#1.py
```

**Compare Output:**
- Total moves in solution path
- Nodes expanded during search
- Traversal steps before goal reached

Observe how GBFS typically expands fewer nodes than BFS, especially on harder puzzles.

## Learning Outcomes

After working through this repository, you should understand:

1. **Uninformed Search:** How BFS and DFS explore state spaces; their guarantees and limitations
2. **Informed Search:** How heuristics guide search; why A* is powerful; memory-time trade-offs
3. **State Space Problems:** How to model puzzles as graphs; representation and efficiency
4. **Algorithm Selection:** When to use BFS (correctness), DFS (memory), or heuristic search (speed)
5. **Practical Constraints:** Why simple algorithms fail on large problems; why heuristics matter in practice

## Implementation Highlights

- **Efficient data structures:** `collections.deque` for O(1) queue operations; `heapq` for priority queues
- **Immutable state representation:** Tuples enable hashing and set membership; critical for visited tracking
- **Parent pointers:** Enable solution path reconstruction in O(d) time and space
- **Exception handling:** Defensive programming in GBFS for robustness
- **Code organization:** Reusable `PuzzleState` class; modular solver implementations

## Files and Execution Paths

**BFS Implementations:**
- `1_BFS/1solved_example.py` — Simple graph BFS
- `1_BFS/2lab_ex.py` — Lab exercise
- `1_BFS/3za_self_question_*.py` — Practice with multiple methods
- `3_Advanced_Algorithms/Solving 8 Puzzle Problem/1_BFS_#1.py` — BFS on 8-puzzle

**DFS Implementations:**
- `2_DFS/1solved_example.py` — Simple recursive DFS
- `2_DFS/1z_solved_example_method*.py` — Alternative iterative approaches
- `2_DFS/5self_question_3_blockchain_DAG_#1.py` — Application to directed acyclic graphs
- `3_Advanced_Algorithms/Solving 8 Puzzle Problem/2_DFS_#1.py` — DFS on 8-puzzle

**Informed Search:**
- `3_Advanced_Algorithms/Solving 8 Puzzle Problem/3_GBFS_#1.py` — Greedy Best-First Search
- `3_Advanced_Algorithms/Solving 8 Puzzle Problem/Other_Algorithms/4_Astar.py` — A* sketch
- `3_Advanced_Algorithms/Solving 8 Puzzle Problem/Other_Algorithms/6_IDA.py` — IDA* sketch

## Further Reading

Each directory contains implementations with inline comments explaining algorithm details. The 8-puzzle README provides deep technical coverage of:
- State representation and immutability
- Neighbor generation and boundary checking
- Heuristic function design
- Complexity analysis (time and space)
- Trade-offs and practical considerations
- Debugging and verification strategies

## Summary

This project provides a progression from fundamental graph search algorithms to sophisticated state-space problem solving. The 8-puzzle serves as a practical, scalable application that demonstrates why uninformed search fails on complex problems and why heuristic-guided algorithms are essential in practice. By comparing BFS, DFS, and GBFS on the same problem, you'll develop intuition for algorithm selection and the fundamental trade-offs in search.
