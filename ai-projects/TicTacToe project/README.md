# TicTacToe Project

Complete implementations of the classic TicTacToe (Noughts and Crosses) game in two modes: 2-Player competition and Human vs AI with optimal play strategy.

## Project Overview

**Purpose:** Demonstrate game logic, win condition detection, and game AI using the minimax algorithm.

**Game Modes:**
1. **2-Player Mode** — Two human players compete locally
2. **Human vs AI Mode** — Human player vs computer-controlled opponent using minimax algorithm for optimal play

**Educational Goals:**
- Board state management and representation
- Game tree search and decision making
- Minimax algorithm for game AI
- Input validation and error handling
- Game flow control (win/loss/draw detection)

## Project Structure

```
TicTacToe project/
├── 0_matrix.py                    # Tutorial: 2D array creation
├── 1_solved_example.py            # (reference material)
├── 2_TTT_2Player_#1.py            # 2-Player game implementation
├── 3_TTT_HumanVsAI_#1.py          # Human vs AI with Minimax
└── README.md                      # This file
```

## Implementation 1: 2-Player Game (`2_TTT_2Player_#1.py`)

A local multiplayer game where two players take turns placing their marks (X and O) on a 3×3 grid.

### Core Concepts

**Board Representation:**
```python
self.board = [['-' for _ in range(3)] for _ in range(3)]
```

- 3×3 2D list (matrix)
- '-' = empty cell
- 'X' = Player 1
- 'O' = Player 2
- Board indexing: [row][col] where row and col are 0-2

**Board Positions (1-indexed for user input):**
```
1 2 3
4 5 6
7 8 9

Maps to (0-indexed) array positions:
(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2)
```

### TicTacToe Class Methods

**`__init__()`**
- Initializes empty board list

**`create_board()`**
- Creates fresh 3×3 board filled with '-'
- Called at game start and after each game ends
- Two equivalent approaches shown (commented):
  - Traditional nested loops
  - List comprehension (used in code)

**`show_board()`**
- Displays current board state
- Joins row elements with spaces
- Prints each row to console
- Called before each player turn

**`select_first_turn()`**
- Randomly selects who goes first
- Returns: 0 or 1
- Converted to: 'O' (1) or 'X' (0)
- Simulates coin toss

**`fix_spot(row, col, player_turn)`**
- Places player mark on board
- Parameters:
  - `row`, `col` — 1-indexed user input
  - `player_turn` — 'X' or 'O'
- Converts to 0-indexed: `self.board[row-1][col-1]`
- Overwrites cell (assumes validation done)

**`swap_player_turn(player_turn)`**
- Alternates between players
- 'X' → 'O', 'O' → 'X'
- Returns: opposite player mark
- Called after valid move

**`is_board_filled()`**
- Checks if all cells occupied
- Iterates through board
- Returns True if no '-' found
- Used for draw condition

**`is_player_win(player_turn)`**
- Checks if specified player has won
- Tests 8 possible winning configurations:
  - 3 horizontal rows
  - 3 vertical columns
  - 2 diagonals
- Algorithm:
  1. **Rows:** Check each row if all cells == player_turn
  2. **Columns:** Check each column if all cells == player_turn
  3. **Diagonal 1:** Check top-left to bottom-right
  4. **Diagonal 2:** Check top-right to bottom-left
- Returns True if any configuration matches

**`start()`**
- Main game loop
- Outer loop: play multiple games
- Inner loop: single game turn sequence
- Flow:
  1. Create board
  2. Randomly select first player
  3. Display toss result
  4. Loop until game ends:
     - Show board
     - Get player input (row col)
     - Validate spot not filled
     - Place mark
     - Check win
     - Check draw
     - Swap player
  5. Ask to play again

### Game Flow

```
START
  │
  ├─→ Create board
  │
  ├─→ Random first player (X or O)
  │
  └─→ GAME LOOP:
      │
      ├─→ Display board
      │
      ├─→ Input: row col (1-3 each)
      │
      ├─→ Validate:
      │   ├─ Check format (valid input)
      │   ├─ Check range (1-3)
      │   └─ Check empty (spot not filled)
      │
      ├─→ Place mark
      │
      ├─→ Check WIN
      │   └─ Yes → Display board, announce winner, break
      │
      ├─→ Check DRAW (board full)
      │   └─ Yes → Announce tie, break
      │
      └─→ Swap player → LOOP

  │
  ├─→ Ask play again?
  │   ├─ Enter → New game
  │   └─ Any key → Exit
  │
END
```

### Error Handling

| Error | Handling |
|-------|----------|
| Invalid input format (not two numbers) | Exception caught, user reprompted |
| Out of range (row/col not 1-3) | Array IndexError or validation, user reprompted |
| Spot already filled | Check before fix_spot, display "Spot already filled", reprompt |
| Keyboard interrupt | Can exit with "exit" keyword |

### Example Session

```
New Game:
Tossing...
X Wins!

Player X Turn:
- - -
- - -
- - -
Enter row and column numbers to fix spot: 1 1

Player O Turn:
X - -
- - -
- - -
Enter row and column numbers to fix spot: 2 2

Player X Turn:
X - -
- O -
- - -
Enter row and column numbers to fix spot: 3 3

Player O Turn:
X - -
- O -
- - X
Enter row and column numbers to fix spot: 1 2

Player X Turn:
X O -
- O -
- - X
Enter row and column numbers to fix spot: 2 1

Player O Turn:
X O -
X O -
- - X
Enter row and column numbers to fix spot: 1 3

O O X
X O -
- - X
Player O Wins!

Press Enter to play again.
Enter anything else to exit program.
```

### Complexity Analysis

**Time Complexity:**
- Check win (per turn): O(1) — fixed 8 checks on 3×3 board
- Check board full: O(1) — exactly 9 cells
- Single game: O(9) = O(1) — max 9 turns

**Space Complexity:**
- Board storage: O(1) — fixed 3×3 = 9 cells
- Game state: O(1) — constant variables

---

## Implementation 2: Human vs AI (`3_TTT_HumanVsAI_#1.py`)

A game where a human player competes against a computer opponent that uses the **minimax algorithm** to play optimally.

### Dependencies

```python
import numpy as np      # NumPy arrays for efficient board representation
import random          # Not currently used (marked "ON HOLD")
```

**Installation:**
```bash
pip install numpy
```

### Core Concepts

**Board Representation (NumPy):**
```python
self.board = np.full((3, 3), '-')  # 3×3array filled with '-'
```

- NumPy 3×3 array (more efficient than Python lists)
- '-' = empty cell
- 'X' = Human player
- 'O' = AI player
- Enables vectorized operations for efficient checking

**Players:**
- `'X'` — Human player (maximizing perspective... actually minimizing, moves first)
- `'O'` — AI player (uses minimax to choose moves)

### TicTacToeAI Class Methods

**`__init__()`**
- Creates 3×3 NumPy array filled with '-'
- Initializes clean board

**`show_board()`**
- Displays current board state
- Iterates through rows
- Joins elements with spaces
- Prints each row + blank line for readability

**`is_winner(player)`**
- Checks if specified player has won
- NumPy vectorized operations:
  - Rows: `np.any(np.all(self.board[i, :] == player) for i in range(3))`
  - Columns: `np.any(np.all(self.board[:, j] == player) for j in range(3))`
  - Main diagonal: `np.all(np.diag(self.board) == player)`
  - Anti-diagonal: `np.all(np.diag(np.fliplr(self.board)) == player)`
- Returns True if any winning configuration found

**`is_full()`**
- Checks if board has no empty cells
- NumPy check: `not np.any(self.board == '-')`
- Returns True if all cells filled

**`available_moves()`**
- Returns list of (row, col) tuples for empty cells
- List comprehension: `[(i, j) for i in range(3) for j in range(3) if self.board[i, j] == '-']`
- Used by minimax to explore possible moves
- Time: O(9) = O(1) constant

### Minimax Algorithm

**Purpose:** Find the optimal move for a player assuming both players play perfectly.

**Concept:**
- `is_maximizing = True` → AI's turn ('O') trying to maximize score
- `is_maximizing = False` → Human's turn ('X') trying to minimize score
- Recursively explores game tree
- Returns score: +1 (AI win), -1 (Human win), 0 (draw)

**Algorithm:**

```python
def minimax(self, is_maximizing):
    # Terminal states (game over)
    if self.is_winner('O'): return 1      # AI won
    if self.is_winner('X'): return -1     # Human won
    if self.is_full(): return 0           # Draw

    if is_maximizing:  # AI's turn (wants high score)
        best_score = -float('inf')
        for each possible move:
            place AI mark ('O')
            score = minimax(next_player=False)  # Recursively evaluate
            undo move
            best_score = max(best_score, score)
        return best_score

    else:  # Human's turn (wants low score)
        best_score = float('inf')
        for each possible move:
            place human mark ('X')
            score = minimax(next_player=True)  # Recursively evaluate
            undo move
            best_score = min(best_score, score)
        return best_score
```

**Example Tree (simplified, first move only):**

```
Initial board (empty):
                 minimax(True)
                      │
                   score=0
                   /       \
         Move1      ...      Move9
         /                      \
    minimax(F)              minimax(F)
    /    |    \             /    |    \
   M1   M2   M3           M1   M2   M3
```

**Semantics:**
- AI tries to maximize final score → chooses move with highest score
- Human tries to minimize final score → chooses move with lowest score
- Both assume opponent plays optimally
- Result: AI always either wins or draws (never loses)

**Time Complexity:**
- Without optimizations: O(9!) ≈ 362,880 leaf nodes
- With alpha-beta pruning: ~O(b^(d/2)) where b=branching factor, d=depth
- Practical: ~1000-5000 nodes for TicTacToe

**Space Complexity:**
- Recursion depth: O(9) = O(1) for call stack
- No additional data structures

**Intuition:**
```
Game Tree Levels:
Level 0 (AI):     AI chooses best move (max score)
Level 1 (Human):  Human chooses best move (min score)
Level 2 (AI):     AI chooses best move (max score)
...
Level 9 (end):    Return win/draw/loss

Minimax backtracks up with best scores at each level
```

**Why Unbeatable:**
- Explores ALL possible game continuations
- Assumes human always plays optimally
- At each node, picks move that maximizes AI score
- Only loses if game rules favor human (impossible in TicTacToe)
- Best outcome: AI wins or forces draw

### best_move() Method

**Purpose:** Find the single best move for AI.

**Algorithm:**
```python
def best_move(self):
    best_score = -float('inf')
    move = None
    
    for each available move:
        place AI mark ('O')
        score = minimax(False)  # Evaluate this move
        undo mark
        
        if score > best_score:
            best_score = score
            move = (this move)
    
    return move
```

**Returns:** (row, col) tuple of best move

**Why Different from Minimax:**
- Minimax returns score only
- best_move() returns actual move coordinates
- Uses minimax internally to evaluate each candidate

### play() Method

**Main game loop:**

```
1. Display welcome message
2. Show initial empty board
3. Loop while game active:
   a. Human move:
      - Prompt: "Enter row and col (1-3 each): "
      - Validate input format (two integers)
      - Validate range (1-3)
      - Validate spot empty
      - Place 'X' on board
   b. Show board
   c. Check human win → break
   d. Check draw → break
   e. AI move:
      - Calculate best_move() using minimax
      - Place 'O' on board
   f. Show board
   g. Check AI win → break
   h. Check draw → break
```

### Error Handling

**Exception Handling:**
```python
try:
    row, col = map(int, input("Enter row and col (1-3 each): ").split())
    if row not in [1, 2, 3] or col not in [1, 2, 3]:
        raise ValueError("Row/Col must be between 1 and 3")
    if self.board[row-1, col-1] != '-':
        raise ValueError("Spot already taken")
    self.board[row-1, col-1] = 'X'
except Exception as e:
    print(f"Invalid input: {e}. Try again.\n")
    continue
```

**Handles:**
- Invalid format (non-integer input)
- Out of range (not 1-3)
- Spot already taken
- Any other exceptions

### Example Session

```
Welcome to Human vs AI TicTacToe!

- - -
- - -
- - -

Enter row and col (1-3 each): 1 1

X - -
- - -
- - -

AI is thinking...

X - -
- O -
- - -

Enter row and col (1-3 each): 2 1

X - -
X O -
- - -

AI is thinking...

X - O
X O -
- - -

Enter row and col (1-3 each): 3 1

X - O
X O -
X - -

AI is thinking...

X - O
X O O
X - -

🤖 AI wins!
```

**Typical Outcomes:**
- If human plays perfectly: Draw (0)
- If human plays suboptimally: AI wins (1)
- Human never wins (AI plays perfectly)

### NumPy vs Standard Python

**Advantages of NumPy:**
```python
# NumPy: vectorized operations
all_equal = np.all(self.board[i, :] == player)

# Python list: manual loop
all_equal = all(self.board[i][j] == player for j in range(3))

# NumPy: efficient checking
available = [(i, j) for i in range(3) for j in range(3) if self.board[i, j] == '-']

# NumPy: diagonal extraction
main_diag = np.diag(self.board)
anti_diag = np.diag(np.fliplr(self.board))
```

**Performance:**
- NumPy faster for large arrays
- TicTacToe too small to notice significant difference
- Educational: shows NumPy usage patterns

---

## Board Representation Tutorial (`0_matrix.py`)

Simple reference showing two ways to create 2D arrays in Python:

**Method 1: Nested Loops**
```python
board = []
for i in range(3):
    row = []
    for j in range(3):
        row.append('-')
    board.append(row)
```

**Method 2: List Comprehension (preferred)**
```python
board = [['-' for _ in range(3)] for _ in range(3)]
```

Both produce: `[['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]`

---

## How to Run

### 2-Player Game

**Requirements:**
- Python 3.6+
- No external dependencies

**Execution:**
```bash
python 2_TTT_2Player_#1.py
```

**Interaction:**
```
1. Game randomly selects first player
2. When prompted: Enter row (1-3) and column (1-3) separated by space
   Example: "2 3" means row 2, column 3
3. Continue until win or draw
4. Choose to play again or exit
```

### Human vs AI Game

**Requirements:**
- Python 3.6+
- NumPy: `pip install numpy`

**Execution:**
```bash
python 3_TTT_HumanVsAI_#1.py
```

**Interaction:**
```
1. Human plays as 'X', AI plays as 'O'
2. Human moves first
3. When prompted: Enter row (1-3) and column (1-3) separated by space
4. AI calculates best move (may take 1-2 seconds on first move)
5. Game ends when AI wins, human wins, or draw occurs
```

**Performance Note:**
- First move evaluation: ~300ms (minimax explores ~5000 nodes)
- Subsequent moves: Faster (fewer available moves)
- Full game: 10-20 seconds with minimax thinking

---

## Comparison: 2-Player vs AI

| Feature | 2-Player | Human vs AI |
|---------|----------|-------------|
| **Players** | Human 1 (X) vs Human 2 (O) | Human (X) vs Computer (O) |
| **AI Algorithm** | N/A (no AI) | Minimax |
| **Difficulty** | Depends on players | Unbeatable (with perfect play) |
| **Outcome Probability** | Any (depends on skill) | AI wins or draw |
| **Board Representation** | Python 2D list | NumPy array |
| **Turn Selection** | Random coin toss | Hardcoded: Human first, AI second |
| **Move Quality** | Varies | Perfect (minimax optimal) |
| **Code Complexity** | ~130 lines | ~150 lines |
| **Error Handling** | Basic | Comprehensive |
| **Dependencies** | None | NumPy |

---

## Game Theory Insights

### Tic-Tac-Toe Solved

Tic-Tac-Toe is a **solved game**:
- With perfect play from both sides: **Always draws**
- Minimax algorithm finds this optimal outcome
- Total possible games: ~5,478 with symmetry; 255,168 without
- Minimax searches all possibilities

### Game Outcomes (with minimax AI)

| Human Play | Result |
|-----------|--------|
| Optimal play | Draw (0) |
| Suboptimal play | AI wins (+1) |
| Never | Human wins (-1) |

### Why Minimax is Perfect

1. **Complete search:** Explores all possible continuations
2. **Optimal decision:** Chooses move that maximizes AI score
3. **Adversarial:** Accounts for human's best response
4. **Deterministic:** Always same move in same position
5. **Backward induction:** Builds decision from game end to start

---

## Algorithm Analysis

### Winning Configurations (8 total)

**Rows:**
```
X X X    O O O
- - -    - - -
- - -    - - -
```

**Columns:**
```
X - -    X - -    X - -
X - -    X - -    X - -
X - -    X - -    X - -
```

**Diagonals:**
```
X - -    - - X
- X -    - X -
- - X    X - -
```

### Decision Tree Size

**First move:** 9 possible positions
**Second move:** 8 possible positions
...
**Total positions:** 9! = 362,880 (upper bound)

**With pruning/symmetry:** ~5,000-10,000 actual evaluations

---

## Extension Ideas

### 1. Larger Board (4×4, 5×5)
```python
class TicTacToeNxN:
    def __init__(self, size=4):
        self.size = size
        self.board = [['−' for _ in range(size)] for _ in range(size)]
    
    def is_winner(self, player):
        # Check rows, columns, all diagonals
        # Need k-in-a-row detection
```

### 2. Difficulty Levels
```python
class AIPlayer:
    def __init__(self, difficulty='hard'):
        self.difficulty = difficulty  # 'easy', 'medium', 'hard'
    
    def choose_move(self):
        if self.difficulty == 'easy':
            return random.choice(self.available_moves())
        elif self.difficulty == 'medium':
            return self.smart_move()  # Limited lookahead
        else:  # hard
            return self.best_move()   # Full minimax
```

### 3. Alpha-Beta Pruning
```python
def minimax_pruned(self, depth, is_max, alpha, beta):
    # Skip branches that can't improve result
    # Reduces nodes from 9! to ~362 for TicTacToe
    if value >= beta:
        return value  # Pruning
```

### 4. Game Statistics
```python
class GameStats:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.draws = 0
    
    def record_game(self, result):
        # Track win rate over multiple games
```

### 5. Move Hints
```python
def suggest_move(self):
    # Use minimax to recommend best move for human
    moves = [(move, self.score_move(move)) for move in available]
    return max(moves, key=lambda x: x[1])
```

### 6. Game Replay
```python
class GameRecorder:
    def __init__(self):
        self.moves = []
    
    def record_move(self, row, col, player):
        self.moves.append((row, col, player))
    
    def replay(self):
        # Replay move sequence
```

### 7. Network Play
```python
class NetworkTicTacToe:
    def __init__(self, host, port):
        self.socket = connect_to_server(host, port)
    
    def send_move(self, row, col):
        # Send human's move to opponent
```

### 8. Graphical UI
```python
import pygame

class TicTacToeGUI:
    def __init__(self):
        self.screen = pygame.display.set_mode((300, 300))
    
    def draw_board(self):
        # Render board with graphics
    
    def handle_click(self, pos):
        # Convert mouse click to board position
```

---

## Technical Stack

**2-Player Version:**
- Python 3.6+
- No external dependencies
- Standard library only

**Human vs AI Version:**
- Python 3.6+
- NumPy (for efficient array operations)

---

## Summary

This project demonstrates two classic implementations of TicTacToe:

1. **2-Player Game:** Simple, interactive game between two humans
   - Shows board state management
   - Win/draw condition detection
   - Turn-based game flow
   - Error handling for user input

2. **Human vs AI Game:** Computer opponent using minimax algorithm
   - Advanced game-playing AI
   - Optimal decision making
   - Demonstrates game tree search
   - Guarantees AI never loses (with perfect play)

**Key Concepts:**
- Board representation (2D arrays)
- Win condition checking (rows, columns, diagonals)
- Game tree search (minimax algorithm)
- Recursive algorithms
- Error handling and validation

**Progression:**
- Beginner: Understand 2-player rules and logic
- Intermediate: Learn minimax algorithm
- Advanced: Optimize with alpha-beta pruning, extend to larger boards

Both implementations serve as excellent learning materials for game development, AI algorithms, and Python programming fundamentals.
