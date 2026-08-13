# AI Search Algorithms and Projects

A comprehensive collection of artificial intelligence implementations covering fundamental graph search algorithms, advanced state-space problem solving, and practical AI applications. This repository demonstrates algorithm design, complexity analysis, and real-world implementations progressing from theoretical concepts to practical systems.

## Repository Overview

```
ai-search-algorithms-and-projects/
├── ai-search-algorithms/           # Core search algorithm implementations
│   ├── 1_BFS/                      # Breadth-First Search fundamentals
│   ├── 2_DFS/                      # Depth-First Search fundamentals
│   ├── 3_Advanced_Algorithms/      # Advanced applications
│   │   └── Solving 8 Puzzle Problem/
│   └── README.md
├── ai-projects/                    # Practical AI applications
│   ├── Attendance System project/
│   ├── Grocery Store Management project (Advanced)/
│   ├── TicTacToe project/
│   ├── Solving 8 Puzzle Problem/
│   └── README.md               
├── LICENSE                         # MIT License
└── README.md                       # This file
```

## Repository Structure

### 1. AI Search Algorithms (`ai-search-algorithms/`)

The core of this repository: comprehensive implementations of graph search and state-space algorithms, progressing from uninformed to informed search strategies.

#### 1.1 Breadth-First Search (`1_BFS/`)

**Purpose:** Demonstrates fundamental BFS concepts on simple graphs.

**Contents:**
- `1solved_example.py` — Classic BFS on a small graph with queue-based exploration
- `2lab_ex.py` — Lab exercise implementing BFS
- `2z_lab_ex_method2_#1.py` — Alternative implementation approach
- `3za_self_question_*.py` — Multiple solution methods to the same BFS problem (3 variations)
- `4self_question_2_#1.py` — Additional practice exercise

**Key Concepts:**
- Queue-based (FIFO) exploration
- Level-by-level graph traversal
- Visited tracking for cycle prevention
- Shortest path guarantee

**Learning Path:** Start with `1solved_example.py`, then work through exercises progressively.

#### 1.2 Depth-First Search (`2_DFS/`)

**Purpose:** Demonstrates DFS variants and depth-first traversal patterns.

**Contents:**
- `1solved_example.py` — Recursive DFS implementation (clean, idiomatic Python)
- `1z_solved_example_method*.py` — Alternative approaches (iterative, different patterns)
- `2lab_ex_.py` — Lab exercise
- `3self_question_1_#1.py` — Practice problem
- `4za_self_question_2_method*.py` — Multiple solutions (3 variations)
- `4zb_self_question_2_method*.py` — Alternative approaches (2 variations)
- `4z_self_question_2_Flowchart.png` — Visual flowchart representation
- `5self_question_3_blockchain_DAG_#1.py` — Application to blockchain/DAG structures
- `5self_question_3.jpeg` — Visual aid for the blockchain problem

**Key Concepts:**
- Recursive and iterative DFS variants
- Stack-based (LIFO) exploration
- Depth-first traversal patterns
- Applications to directed acyclic graphs (DAGs) and blockchain

**Learning Path:** Compare recursive vs. iterative implementations; see how DFS applies to blockchain structures.

#### 1.3 Advanced Algorithms (`3_Advanced_Algorithms/`)

**Solving 8 Puzzle Problem — Complete Implementation**

A full-featured implementation of the classic 8-puzzle problem using multiple search algorithms. This demonstrates how algorithms scale from simple graphs to complex state spaces with 181,440 reachable states.

**Algorithms Implemented:**
- **BFS** (`1_BFS_#1.py`) — Optimal but memory-intensive; guaranteed shortest solution
- **DFS** (`2_DFS_#1.py`) — Memory-efficient but suboptimal; explores depth-first
- **Greedy Best-First Search** (`3_GBFS_#1.py`) — Fast heuristic-guided search; may sacrifice optimality
- **Custom Algorithm** (`3_my_own_algorithm.py`) — Experimental variant combining greedy and branch-and-bound (incomplete)

**Advanced Sketches** (`Other_Algorithms/`):
- **A\*** (`4_Astar.py`) — Combines actual cost + heuristic; optimal and informed
- **Uniform Cost Search** (`5_UCS.py`) — Path cost only; optimal but uninformed
- **Iterative Deepening A\*** (`6_IDA.py`) — Memory-efficient alternative to A*
- **Dijkstra** (`7_Dijkstra.py`) — Sketch/documentation

**Problem Formulation:**
- 3×3 grid with tiles 1-8 and one empty space (0)
- Actions: slide a tile into the empty space (up, down, left, right)
- State space: 181,440 reachable configurations (9!/2)
- Goal: transform initial configuration to target configuration

**Key Implementation Details:**
- **State Representation:** Immutable tuple-of-tuples for hashing and set membership
- **Neighbor Generation:** Valid moves within 3×3 grid boundaries
- **Heuristics:** Misplaced tiles and Manhattan distance
- **Data Structures:** Deque for BFS/DFS, heapq for priority queues
- **Path Reconstruction:** Parent pointers for O(d) solution backtracking

**Algorithm Comparison (8-Puzzle Example):**
| Algorithm | Optimal | Complete | Memory | Speed | Example Stats |
|-----------|---------|----------|--------|-------|---------------|
| BFS | ✓ | ✓ | O(b^d) | Moderate | ~48 nodes, 4 moves |
| DFS | ✗ | ✗ | O(d) | Variable | ~60+ nodes, 4+ moves |
| GBFS | ✗ | ✗ | O(b^d) | Fast | ~20 nodes, 4 moves |
| A* | ✓ | ✓ | O(b^d) | Fast | Sketch only |
| IDA* | ✓ | ✓ | O(d) | Slower | Sketch only |

**For detailed implementation information: See [ai-search-algorithms/3_Advanced_Algorithms/Solving 8 Puzzle Problem/README.md](ai-search-algorithms/3_Advanced_Algorithms/Solving%208%20Puzzle%20Problem/README.md)**

### 2. AI Projects (`ai-projects/`)

Practical applications demonstrating AI concepts in realistic scenarios: attendance tracking, store management, game playing, and state-space problem solving.

#### 2.1 Attendance System Project

**Purpose:** Automated student attendance tracking system with course management and performance analysis.

**Files:**
- `exercise.py` — Complete working implementation (~60 lines)
  - `Student` class for individual tracking
  - `AttendanceTracker` class for system management
  - Full session/attendance calculation and grouping logic
- `src/main.py` — Interactive framework (skeleton/incomplete)
  - `AttendanceManager` class for extended functionality
  - Stub methods for future expansion
- `src/courses.json` — Pre-defined course data
  - Courses: Robotics, AI, A&D Electronics, BMFA, Machine Drawing
  - Session counts for each course

**Key Features:**
- **Attendance Calculation:** `(present_days / total_sessions) × 100`, rounded to 2 decimals
- **Automatic Grouping:** 
  - Group 1: 91-100% attendance (excellent)
  - Group 2: 75-90% attendance (good)
  - Group 3: 60-75% attendance (satisfactory)
  - Group 4: <60% attendance (needs improvement)
- **Data Management:**
  - Add students dynamically
  - Track attendance per session
  - Persistent storage via JSON
- **Reporting:**
  - Display attendance summary with percentages
  - Display students grouped by performance
  - Formatted table output for readability

**Example Output:**
```
Attendance Summary:
┌─────────┬─────────┬───────────────┬──────────────┐
│ Student │ Present │ Total Session │ Attendance % │
├─────────┼─────────┼───────────────┼──────────────┤
│ Alice   │ 18      │ 20            │ 90.00%       │
│ Bob     │ 14      │ 20            │ 70.00%       │
└─────────┴─────────┴───────────────┴──────────────┘

Grouped by Performance:
Group 1 (91-100%): Alice
Group 2 (75-90%): 
Group 3 (60-75%): Bob
Group 4 (<60%):
```

**Key Concepts:** Object-oriented design, data structures (dictionaries, lists), class methods, data persistence, performance calculations

**Learning Outcomes:** Class design, method organization, data grouping algorithms, JSON file handling

#### 2.2 Grocery Store Management Project (Advanced)

**Purpose:** Comprehensive point-of-sale and inventory management system with multi-format data support and transaction history.

**Implementations:**
1. **Simple Version** (`exercise.py`) — ~70 lines
   - Hardcoded product catalog
   - Interactive checkout workflow
   - Alphabetical bill sorting
   - Uses `tabulate` for formatted output
   
2. **Advanced Version** (`src/grocery_intermediate.py`) — ~300 lines
   - Production-ready system
   - Multi-format catalog support (JSON/CSV)
   - SQLite database for transaction persistence
   - Full discount and tax calculation
   - PDF and CSV export capabilities
   - Comprehensive error handling

**Files:**
- `exercise.py` — Simple implementation (learning-focused)
- `README.md` — Complete project documentation
- `src/` — Source modules and data
  - `grocery_intermediate.py` — Advanced implementation
  - `grocery.json` — Product catalog (JSON format)
  - `grocery.csv` — Product catalog (CSV format)
  - `customer_bill.csv` — Generated billing records
  - `grocery_records.db` — SQLite transaction history
  - `customer_bill.pdf` — Generated receipt (PDF)

**Key Features (Advanced):**
- **GroceryStore Class:**
  - Multi-format catalog loader (JSON/CSV auto-detection)
  - Case-insensitive product search
  - Robust error handling for missing/corrupted data
  
- **Bill Class:**
  - Interactive item addition with quantity
  - Discount application (percentage-based)
  - Tax/GST calculation
  - Bill persistence to SQLite database
  - Export to CSV and PDF formats
  
- **Data Management:**
  - SQLite schema with `bills` and `bill_items` tables
  - Foreign key relationships for data integrity
  - Timestamp tracking for all transactions
  - Supports multiple customers per session

- **Multi-Format Support:**
  - JSON: Structured, human-readable catalog
  - CSV: Spreadsheet-compatible format
  - Automatic format detection and parsing

**Example Workflow:**
```
1. Load product catalog (JSON or CSV)
2. Display available items with prices
3. Interactive checkout:
   - Add items with quantities
   - Validate each item exists
4. Apply discount (optional)
5. Apply GST/Tax (optional)
6. Display formatted bill
7. Save to database
8. Export to CSV and PDF
9. Next customer (loop)
```

**Sample Bill Output:**
```
┌───────────────┬─────┬──────────┬────────────┐
│ Item          │ Qty │ Price    │ Cost (Rs.) │
├───────────────┼─────┼──────────┼────────────┤
│ Rice          │ 5   │ 50       │ 250        │
│ Milk          │ 2   │ 25       │ 50         │
│ Bread         │ 3   │ 30       │ 90         │
└───────────────┴─────┴──────────┴────────────┘

Discount Applied: Rs.46.40 (10%)
GST Applied: Rs. 83.16 (18%)
Grand Total: Rs. 376.76
```

**Key Concepts:** 
- Object-oriented design (GroceryStore, Bill classes)
- File I/O (JSON, CSV, SQLite, PDF)
- Data validation and error handling
- Business logic (discounts, tax calculations)
- Database design and persistence
- Multi-format data handling

**Technical Complexity:**
- **Simple version:** Beginner (hardcoded, basic logic)
- **Advanced version:** Intermediate-Advanced (production-ready, enterprise patterns)

**Learning Outcomes:** 
- Class design and relationships
- File format handling (JSON, CSV, PDF)
- Database operations and schema design
- Error handling strategies
- Real-world system architecture

#### 2.3 TicTacToe Project

**Purpose:** Classic game implementation demonstrating game AI and decision-making algorithms.

**Files:**
- `0_matrix.py` — Tutorial: 2D array creation patterns
- `1_solved_example.py` — Reference implementation
- `2_TTT_2Player_#1.py` — Two-player mode (human vs. human)
- `3_TTT_HumanVsAI_#1.py` — Human vs. AI mode with minimax algorithm
- `README.md` — Comprehensive project documentation

**Implementation 1: Two-Player Mode (`2_TTT_2Player_#1.py`)**

**TicTacToe Class Methods:**
- `create_board()` — Initialize 3×3 grid
- `show_board()` — Display current board state
- `fix_spot(row, col, player)` — Place mark on board
- `is_player_win(player)` — Check win condition (8 configurations)
- `is_board_filled()` — Detect draw condition
- `swap_player_turn()` — Alternate between players
- `select_first_turn()` — Random coin toss for first player

**Game Flow:**
```
1. Create empty 3×3 board
2. Randomly select first player (X or O)
3. Loop until game ends:
   - Display board
   - Get player input (row, col)
   - Validate: format, range, empty spot
   - Place mark
   - Check win → break if won
   - Check draw → break if board full
   - Swap player
4. Ask to play again
```

**Win Detection:**
- 3 horizontal rows
- 3 vertical columns
- 2 diagonals (main and anti-diagonal)
- Total: 8 possible winning configurations

**Error Handling:**
- Invalid input format (non-integers)
- Out-of-range (not 1-3)
- Spot already filled
- Keyboard interrupts

**Implementation 2: Human vs AI Mode (`3_TTT_HumanVsAI_#1.py`)**

**Core AI: Minimax Algorithm**

The `TicTacToeAI` class uses NumPy arrays and implements the minimax algorithm for perfect play.

**Minimax Concept:**
- Explores entire game tree recursively
- AI (player 'O') maximizes score
- Human (player 'X') minimizes score
- Score: +1 (AI wins), -1 (human wins), 0 (draw)
- Both players assumed to play optimally
- Result: AI never loses (always draws at worst)

**Algorithm Structure:**
```
minimax(is_maximizing):
  if game over:
    return score (1, -1, or 0)
  
  if AI's turn (maximizing):
    best_score = -infinity
    for each possible move:
      place AI mark
      score = minimax(next=human)
      undo mark
      best_score = max(best_score, score)
    return best_score
  
  else (human's turn, minimizing):
    best_score = +infinity
    for each possible move:
      place human mark
      score = minimax(next=AI)
      undo mark
      best_score = min(best_score, score)
    return best_score
```

**Key Methods:**
- `is_winner(player)` — Check win using NumPy vectorized ops
- `is_full()` — Check board full using NumPy any()
- `available_moves()` — Return list of empty positions
- `minimax(is_maximizing)` — Recursive game tree evaluation
- `best_move()` — Find optimal move using minimax
- `play()` — Main game loop with error handling

**Game Flow:**
```
1. Human plays as 'X', AI plays as 'O'
2. Human moves first
3. Loop until game ends:
   - Human enters row and col (1-3)
   - Validate input
   - Place 'X' on board
   - Check win/draw
   - AI calculates best move using minimax
   - Place 'O' on board
   - Check win/draw
```

**Performance:**
- First move evaluation: ~300ms (explores ~5,000 nodes)
- Subsequent moves: Faster (fewer available positions)
- Full game: 10-20 seconds total
- Complete search: 9! = 362,880 worst case; ~5,000 with strategy

**Why Unbeatable:**
- Minimax is mathematically complete
- Explores ALL possible game continuations
- Chooses move that maximizes AI advantage
- Tic-Tac-Toe is "solved" — perfect play = draw

**Typical Outcomes:**
- Perfect human play → Draw (0)
- Suboptimal human play → AI wins (+1)
- Human never wins (-1)

**Key Concepts:**
- 2D array/matrix representation
- Win condition checking (8 patterns)
- Game tree search algorithms
- Minimax algorithm (adversarial search)
- Recursive evaluation
- NumPy for efficient array operations
- Game theory and optimal play

**Learning Outcomes:**
- Game AI principles
- Recursive algorithms
- Board game logic and state management
- Algorithm optimization (minimax)
- Adversarial reasoning

**Comparison: 2-Player vs AI**
| Aspect | 2-Player | vs AI |
|--------|----------|-------|
| Difficulty | Depends on players | Unbeatable |
| Algorithm | None (manual) | Minimax |
| Data Structure | Python list | NumPy array |
| Outcome | Any | AI wins or draw |
| Execution | Instant | ~300ms per move |

#### 2.4 Solving 8 Puzzle Problem (Project Version)

A dedicated project implementation of the 8-puzzle state-space problem, complementing the algorithm-focused version in `ai-search-algorithms/3_Advanced_Algorithms/`.

**Files:**
- `1_BFS_#1.py` — BFS solver (optimal, memory-intensive)
- `2_DFS_#1.py` — DFS solver (memory-efficient)
- `3_GBFS_#1.py` — Greedy Best-First Search (fast heuristic-guided)
- `3_my_own_algorithm.py` — Experimental hybrid variant
- `Other_Algorithms/` — Advanced sketches
  - `4_Astar.py` — A* (optimal + informed)
  - `5_UCS.py` — Uniform Cost Search
  - `6_IDA.py` — Iterative Deepening A*
  - `7_Dijkstra.py` — Reference implementation
- `README.md` — Full technical documentation

**Problem Definition:**
```
Initial State:
  1 2 3
  4 0 5      (0 = empty space)
  7 8 6

Goal State:
  1 2 3
  4 5 6
  7 8 0

Actions: Slide tile into empty space (up, down, left, right)
State Space: 181,440 reachable configurations (9!/2)
Solution Depth: Typically 4-20 moves depending on puzzle difficulty
```

**Algorithm Comparison (same puzzle):**
| Algorithm | Nodes | Moves | Memory | Time | Status |
|-----------|-------|-------|--------|------|--------|
| BFS | ~48 | 4 | High | Moderate | Optimal ✓ |
| DFS | ~60+ | 4+ | Low | Variable | Suboptimal |
| GBFS | ~20 | 4 | Medium | Fast | Suboptimal |
| A* | Fewer | 4 | Moderate | Fast | Optimal ✓ |
| IDA* | ~50 | 4 | Low | Slower | Optimal ✓ |

**Key Implementation Details:**
- State representation: Immutable tuples (hashable for visited sets)
- Move generation: Valid tiles adjacent to empty space
- Heuristics: Misplaced tiles, Manhattan distance
- Data structures: Deque (BFS/DFS), heapq (priority queues)
- Path reconstruction: Parent pointers for O(d) backtracking

**Use Cases:**
- Compare algorithm performance on same problem
- Understand state-space search trade-offs
- Study heuristic effectiveness
- Benchmark optimization techniques

**For detailed algorithm analysis: See [ai-search-algorithms/3_Advanced_Algorithms/Solving 8 Puzzle Problem/README.md](ai-search-algorithms/3_Advanced_Algorithms/Solving%208%20Puzzle%20Problem/README.md)**

### 3. Lab Manual and Exercises (`1AI_Lab_Mannual/`)

Supporting materials for learning and practice.

**Files:**
- `1AI lab mannual.pdf` — Lab manual documentation (PDF)
- `1practice.py` — Practice exercises
- `creating_folders_final.py` — Utility for directory setup

**Purpose:** Supplementary learning materials accompanying the main implementations.

## Technology Stack

- **Language:** Python 3.6+
- **Dependencies:** Standard library only
  - `collections.deque` — Efficient queue/stack operations
  - `heapq` — Priority queue for informed search
  - `itertools.count()` — Tie-breaking in heaps
  - `json` — Data persistence (projects)
  - `csv` — Transaction logging (projects)

## Algorithm Summary

### Uninformed (Blind) Search

**Breadth-First Search (BFS)**
- Explores level-by-level using a queue
- **Optimal:** Yes (shortest path)
- **Complete:** Yes (if solution exists)
- **Space:** O(b^d) — exponential
- **Time:** O(b^d) — exponential
- **Best For:** Small problems requiring guaranteed optimal solution

**Depth-First Search (DFS)**
- Explores depth-first using a stack or recursion
- **Optimal:** No (may find suboptimal paths)
- **Complete:** No (without cycle detection, may loop)
- **Space:** O(d) — linear in depth
- **Time:** O(b^m) — depends on depth
- **Best For:** Memory-constrained scenarios; optimality not required

### Informed (Heuristic) Search

**Greedy Best-First Search (GBFS)**
- Explores states by lowest heuristic value
- **Optimal:** No (heuristic may mislead)
- **Complete:** No (may fail on certain topologies)
- **Space:** O(b^d) — but pruned by heuristic
- **Time:** Fast in practice with good heuristics
- **Best For:** Speed important; good heuristics available; optimality not critical

**A\*** (Sketch)
- Combines actual cost (g) + heuristic (h): f(n) = g(n) + h(n)
- **Optimal:** Yes (with admissible heuristic)
- **Complete:** Yes
- **Space:** O(b^d)
- **Time:** Fast with good heuristics
- **Best For:** Optimal solutions with heuristic guidance

**Iterative Deepening A\*** (Sketch)
- IDA* combines iterative deepening with A*
- **Optimal:** Yes
- **Complete:** Yes
- **Space:** O(d) — major advantage over A*
- **Time:** Slower than A* due to recalculation
- **Best For:** Memory-critical applications; optimal solution required

## How to Use This Repository

### 1. Learn Search Algorithms

**Start with fundamentals:**
```bash
cd ai-search-algorithms/1_BFS
python 1solved_example.py        # Simple BFS on graph

cd ../2_DFS
python 1solved_example.py        # Simple recursive DFS
```

**Progress to advanced:**
```bash
cd ../3_Advanced_Algorithms/Solving\ 8\ Puzzle\ Problem
python 1_BFS_#1.py               # BFS on 8-puzzle (optimal but slow)
python 3_GBFS_#1.py              # GBFS on 8-puzzle (fast heuristic-guided)
```

### 2. Compare Algorithm Performance

Run the same problem with different algorithms and observe:
- **Nodes expanded:** How many states were explored?
- **Solution length:** How many moves in the solution?
- **Memory usage:** BFS stores more states than DFS
- **Execution time:** GBFS typically faster than BFS on hard problems

Example comparison:
```bash
# In Solving 8 Puzzle Problem directory
python 1_BFS_#1.py     # Output: ~48 nodes, 4 moves
python 3_GBFS_#1.py    # Output: ~20 nodes, 4 moves
```

### 3. Explore AI Projects

Run practical applications:
```bash
cd ai-projects/Attendance\ System\ project
python exercise.py

cd ../Grocery\ Store\ Management\ project\ \(Advanced\)
python exercise.py

cd ../TicTacToe\ project
python 3_TTT_HumanVsAI_#1.py
```

### 4. Study Problem-Specific Solutions

Each project folder contains:
- Multiple implementation approaches
- Solved examples with explanations
- Practice exercises with variations
- Visual aids (flowcharts, diagrams)

## Key Insights and Learning Outcomes

### From BFS/DFS Fundamentals
1. **Exploration Strategies:** Different orderings (queue vs. stack) lead to different solutions
2. **Cycle Prevention:** Visited sets prevent infinite loops
3. **Optimality:** BFS guarantees shortest path; DFS does not
4. **Space Trade-offs:** DFS uses O(d) space; BFS uses O(b^d)

### From Advanced Algorithms
1. **State Space Explosion:** Simple problems (puzzles) have large state spaces (181,440 states for 8-puzzle)
2. **Heuristic Power:** Good heuristics (Manhattan distance) reduce search by 50-100×
3. **Algorithm Selection:** No algorithm is universally best; choice depends on problem constraints
4. **Practical Constraints:** Real systems often use heuristics even if they sacrifice theoretical optimality

### From Projects
1. **Real-World Complexity:** Practical AI involves data management, UI, persistence
2. **Game AI:** Minimax and game trees enable competitive play
3. **System Design:** Clean architecture enables extensibility and maintenance
4. **Testing Strategies:** Multiple implementations and test cases verify correctness

## Code Organization and Design Patterns

- **Composition over Inheritance:** Solver classes contain PuzzleState instances
- **Immutable State:** Tuples enable hashing and efficient visited tracking
- **Parent Pointers:** Enable O(d) solution path reconstruction
- **Modular Structure:** Reusable components across different solvers
- **Exception Handling:** Defensive programming in error-prone operations
- **Clear Naming:** Files indicate approach (method1, method2) for comparison

## File Naming Convention

- `1` prefix — Solved examples or introductory material
- `2` prefix — Lab exercises or intermediate problems
- `3` prefix — Self-questions or more advanced problems
- `4`, `5` — Additional exercises and applications
- `#1`, `method1/2/3` — Alternative approaches to same problem
- `_final` — Polished or complete version

## Running All Examples

**For quick overview:**
```bash
python ai-search-algorithms/1_BFS/1solved_example.py
python ai-search-algorithms/2_DFS/1solved_example.py
python ai-search-algorithms/3_Advanced_Algorithms/Solving\ 8\ Puzzle\ Problem/1_BFS_#1.py
```

**For comprehensive testing:**
```bash
# Test all BFS variations
for file in ai-search-algorithms/1_BFS/*.py; do
    echo "Running $file"
    python "$file"
done

# Test all DFS variations
for file in ai-search-algorithms/2_DFS/*.py; do
    echo "Running $file"
    python "$file"
done
```

## Project Focus Areas

| Area | Files | Complexity |
|------|-------|-----------|
| **Graph Search** | `1_BFS/*`, `2_DFS/*` | Beginner |
| **State-Space Search** | `3_Advanced_Algorithms/Solving 8 Puzzle Problem/*` | Intermediate |
| **Practical Systems** | `ai-projects/Attendance/*`, `ai-projects/Grocery/*` | Intermediate |
| **Game AI** | `ai-projects/TicTacToe/*` | Intermediate |
| **Algorithm Comparison** | Multiple implementations of same problem | Advanced |

## Performance Characteristics

### 8-Puzzle Example (4-move solution)

| Algorithm | Nodes Expanded | Solution Moves | Memory | Time |
|-----------|--|--|--|--|
| BFS | ~48 | 4 (optimal) | High | Moderate |
| DFS | ~60+ | 4+ (not optimal) | Low | Variable |
| GBFS | ~20 | 4 | Medium | Fast |

### Scaling to Harder Problems

- **10-move solution:** BFS explores ~10,000 states; GBFS ~200-500
- **20-move solution:** BFS explores ~1M+ states; GBFS ~1,000-5,000
- **50-move solution:** BFS infeasible; DFS unreliable; GBFS/A* practical

## Documentation

Each major directory contains a detailed README:
- [ai-search-algorithms/README.md](ai-search-algorithms/README.md) — Algorithm overview and learning paths
- [ai-search-algorithms/3_Advanced_Algorithms/Solving 8 Puzzle Problem/README.md](ai-search-algorithms/3_Advanced_Algorithms/Solving%208%20Puzzle%20Problem/README.md) — Deep technical analysis
- [ai-projects/README.md](ai-projects/README.md) — Project descriptions

## License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

Copyright © 2026

## Summary

This repository is a comprehensive learning and reference resource for AI algorithms and applications:

1. **Foundations:** BFS and DFS on simple graphs teach core concepts
2. **Advanced Applications:** 8-puzzle demonstrates scaling and optimization
3. **Practical Systems:** Projects show real-world AI implementations
4. **Comparative Analysis:** Multiple approaches to same problems enable understanding
5. **Production Insights:** Trade-offs between optimality, memory, and speed

The progression from theoretical graph algorithms to practical applications provides both understanding and implementation skills essential for AI development.
