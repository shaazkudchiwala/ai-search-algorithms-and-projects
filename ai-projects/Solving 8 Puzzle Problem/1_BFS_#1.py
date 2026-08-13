from collections import deque
import copy

#Eight Puzzle Problem is a directed graph

class PuzzleState:

    def __init__(self, board, empty_pos, moves=0, parent=None):
        self.board = tuple(tuple(row) for row in board)
        self.moves = moves
        self.parent = parent
        self.empty_pos = empty_pos

    def __repr__(self):
        # for row in self.board:
        #     print("  ".join(map(str, row)))
        return "\n".join("  ".join(map(str, row)) for row in self.board)
    
    def get_neighbours(self):
        """Generate all possible moves from current state"""
        x, y = self.empty_pos
        directions = ((-1,0), (1,0), (0,-1), (0,1))     #up, down, left, right (row, column)
        neighbours = []

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x <= 2 and 0 <= new_y <= 2 :
                # new_board = copy.deepcopy(self.board)     ##Too expensive
                new_board = list(list(row[:]) for row in self.board)

                # swap empty tile with neighbor
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                
                new_board = tuple(tuple(row) for row in new_board)  #back to tuple

                # appending all new_board one by one as Objects to the neighbours list:
                neighbours.append(PuzzleState(new_board, (new_x, new_y), self.moves+1, self))   #here self is given as parent. 
        return neighbours
    
    def __eq__(self, other):
        return self.board == other.board
    
    def __hash__(self):    # other
        # return hash(str(self.board))
        # return hash(tuple(map(tuple, self.board)))
        return hash(self.board)     #Since we're using puzzle board as tuple of tuples already, it is already hashable


class PuzzleSolverBFS:      #self = puzzle1; puzzle1 is an object of PuzzleSolverBFS

    def __init__(self, initial, final):
        self.initial = PuzzleState(initial, self.find_empty_tile(initial))    #self.initial becomes an object of PuzzleState
        # self.final = PuzzleState(final, self.find_empty_tile(final))
        self.final = PuzzleState(final, None)


    # Automatically detect empty position.
    def find_empty_tile(self, board):
        for row_idx, row in enumerate(board):
            for col_idx, item in enumerate(row):
                if item == 0:
                    return (row_idx, col_idx)   #Tuple
        raise ValueError("No empty tile (0) found in the board")

    #Main BFS
    def solve(self):
        queue = deque([self.initial])
        visited = {self.initial}
        traversal_order = []
        nodes_expanded = 0

        while queue:
            state = queue.popleft()
            traversal_order.append(state)
            nodes_expanded += 1

            if state.board == self.final.board:     #self.final is an object of PuzzleState class, and so is state
                print("✅ Goal reached using BFS!\n")
                self.print_stats(state, traversal_order, nodes_expanded)
                return
            
            for neighbour in state.get_neighbours():
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        print("❌ No solution found with BFS.")
    
    
    def print_stats(self, state, traversal_order, nodes_expanded):
        print("Traversal Order (BFS expansion):")
        for idx, s in enumerate(traversal_order):
            print(f"\nStep {idx}:\n{s}")
            steps = idx
    
        print("\n\nShortest Possible Path (After backtracking):")   #Only up, down, left, right movements allowed. Solution Path.
        path = []
        while state is not None:
            path.append(state)
            state = state.parent
        path.reverse()
        for idx, s in enumerate(path):
            print(f"Move {idx}:\n{s}\n")

        print(f"Total Moves (in Solution Path): {len(path)-1}")
        print(f"BFS traversal Steps: {steps}")
        print(f"Total Nodes Expanded (Search Effort): {nodes_expanded}")      

            


# Example run
initial = [[1, 2, 3],
           [5, 6, 0],
           [7, 8, 4]]

final = [[1, 2, 3],
         [5, 8, 6],
         [0, 7, 4]]



puzzle1 = PuzzleSolverBFS(initial, final)
if __name__ == "__main__":
    puzzle1.solve()



# Random Note:
# The else block on a for loop executes only if the loop runs to completion without a break.
# If the loop breaks early → the else block is skipped.
