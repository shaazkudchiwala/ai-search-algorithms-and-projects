from collections import deque
import copy


# Board = Cnfiguration of a puzzle
# State = A whole set of properties (including Board, parent_tacking) of a PuzzleBoard with a unique hash, or we can say PuzzleState.

# PuzzleState class ka object is basically one full puzzle board, where board attr just represents the configuration of the puzzle board which is one of it's many properties.
# We're using PuzzleSolverDFS as just a class with functions to follow DFS algorithm and basically the solution we want to show as output. We use objects of PuzleState class to better navigate the solution.


#Output:
# Total Moves (in Solution Path): 51549
# BFS transveral Steps: 58701
# Total Nodes Expanded (Search Effort): 58702


class PuzzleState:
    def __init__(self, board, empty_pos, moves=0, parent=None):    #Eg of self: Object of board config- self.starting, And in self.starting, self is probably puzzle1. 
        self.board = tuple(tuple(row) for row in board)
        self.empty_pos = empty_pos
        self.moves = moves
        self.parent = parent

    def __repr__(self):
        return "\n".join("  ".join(map(str, row)) for row in self.board) + "\n"
        
    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        # return hash(tuple(map(tuple, self.board)))
        return hash(self.board)     #Since we're using puzzle board as tuple of tuples already, it is already hashable


    def get_neighbours(self):
        """Generate all possible moves from current state"""
        x, y = self.empty_pos
        directions = ((-1,0), (1,0), (0,-1), (0,1))     #up, down, left, right (row, column)
        neighbours = []

        for dx, dy in directions:
            n = 3   # n*n - 1 puzzle
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < n and 0 <= new_y < n :
                # new_board = copy.deepcopy(self.board)  ##Too expensive
                new_board = list(list(row[:]) for row in self.board)

                # swap empty tile with neighbor
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                
                new_board = tuple(tuple(row) for row in new_board)
                
                neighbours.append(PuzzleState(new_board, (new_x, new_y), self.moves+1, self))
        return neighbours


class PuzzleSolverDFS:
    def __init__(self, starting_board, goal_board):
        self.starting_state = PuzzleState(starting_board, self.find_empty_tile_pos(starting_board))
        self.goal_state = PuzzleState(goal_board, None)   #  an attribute (self.goal_state) of a class (PuzzleSolverdDFS) being an object of another class (PuzzleState) is called composition.


    def find_empty_tile_pos(self, board):
        empty_tiles = 0
        for row_index, row in enumerate(board):
            for col_index, item in enumerate(row):
                if item == 0:
                    empty_tiles += 1
                    pos = (row_index, col_index)
        if empty_tiles == 1:
            return pos
        elif empty_tiles == 0:
            raise ValueError("No Empty Tile (0) found.")
        else:
            raise ValueError("More than one empty (0) tiles.")
        
    #Main DFS
    def solve(self):
        stack = deque([self.starting_state])
        visited = {self.starting_state}     
        traversal_path = []   
        nodes_expanded = 0

        while stack:
            popped_state = stack.pop()
            traversal_path.append(popped_state)
            nodes_expanded += 1

            if popped_state == self.goal_state:
                print("✅ Goal reached using DFS!\n")
                self.show_stats(popped_state, traversal_path, nodes_expanded)
                return
            
            for neighbour in popped_state.get_neighbours():
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)

        print("❌ No solution found with DFS.")


    def show_stats(self, state, traversal_path, nodes_expanded):
        print("\nTraversal Order (DFS expansion):")
        for index, state in enumerate(traversal_path):
            print(f"\nStep {index}:\n{state}")

        # Note: We do not find shortest path by backtracking DFS transversed nodes. So we skip that part.

        print(f"DFS traversal Steps: {len(traversal_path) - 1}")
        print(f"Total Nodes Expanded (Search Effort): {nodes_expanded}")





#Example Run
starting_board = [[1, 2, 3],
                  [5, 6, 0],
                  [7, 8, 4]]

goal_board = [[1, 2, 3],
              [5, 8, 6],
              [0, 7, 4]]

puzzle1 = PuzzleSolverDFS(starting_board, goal_board)

if __name__ == "__main__":
    puzzle1.solve()


#Output:
# Total Moves (in Solution Path): 51549
# BFS transveral Steps: 58701
# Total Nodes Expanded (Search Effort): 58702