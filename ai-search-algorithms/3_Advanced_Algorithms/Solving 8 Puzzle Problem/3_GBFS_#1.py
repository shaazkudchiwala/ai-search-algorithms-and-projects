# Greedy Best First Search Algorithm
# Cost function: f(n) = h(n)
# h(n) = here, no. of misplaced tiles

import heapq
import itertools

n=3

class PuzzleState:
    def __init__(self, board, empty_pos, goal_board, moves=0, parent=None):

        if not (isinstance(board, tuple) and all(isinstance(row, tuple) for row in board)):
            self.board = tuple(tuple(row) for row in board)
        else:
            self.board = board

        self.empty_pos = empty_pos
        self.moves = moves
        self.parent = parent

        self.cost = self.CalculateCost(goal_board)
        self.goal_board = goal_board

    def __repr__(self):
        return "\n".join("  ".join(map(str, row)) for row in self.board)
        
    def __eq__(self, other):
        return self.board == other.board
    
    ## Alternative to using itertools
    # def __lt__(self, other):
    #     return self.cost < other.cost
    
    def __hash__(self):
        return hash(self.board)
    
    def CalculateCost(self, goal_board):
        # state_cost = g + h (in A*) where g = self.moves
        # state_cost = h (in GreedyBFS)

        # n=3
        h=0
        # Finding number of misplaced tiles (h)
        for i in range(n):
            for j in range(n):
                # if (self.board[i][j] == goal_board[i][j] and self.board[i][j] == 0):
                #     pass
                # else:
                #     h += 1
                if (self.board[i][j] != goal_board[i][j] and self.board[i][j] != 0):
                    h += 1
        self.cost = h
        return self.cost

    
    def get_neighbours(self):
        try:
            x, y = self.empty_pos
            directions = ((-1,0), (1,0), (0,-1), (0,1))  #up, down, left, right
            neighbours = []
            # n = 3

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if (0 <= new_x < n) and (0 <= new_y < n):
                    new_board = list(list(row[:]) for row in self.board)    #copying as list of list
                    new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]     #Making changes (swapping)
                    new_board = tuple(tuple(row) for row in new_board)      #back to tuple of tuples

                    new_board = PuzzleState(new_board, (new_x, new_y), self.goal_board, self.moves+1, self)
                    neighbours.append((new_board.cost, new_board))  #Tuple
            return neighbours
        
        except Exception as e:
            raise RuntimeError(f"Solver failed due to error: {e}")


class PuzzleSolverGreedyBFS:
    def __init__(self, starting_board, goal_board, initial_cost=0):
        self.starting_state = PuzzleState(starting_board, self.find_empty_tile_pos(starting_board), goal_board)
        self.goal_board = tuple(tuple(row) for row in goal_board)
        self.initial_cost = initial_cost

    def find_empty_tile_pos(self, board):
        empty_tiles = 0
        for row_index, row in enumerate(board):
            for col_index, item in enumerate(row):
                if item == 0:
                    empty_tiles += 1
                    pos = (row_index, col_index)    #Tuple
        if empty_tiles == 1:
            return pos
        elif empty_tiles == 0:
            raise ValueError("No Empty Tile (0) found.")
        else:
            raise ValueError("More than one empty (0) tiles.")
        
    def show_stats(self, state, path, cost, nodes_expanded):
        print("\nGreedy Best First Search Path:")
        for index, s in enumerate(path):
            print(f"\nStep {index}:\n{s}")

        # # Backtracking: Correct
        # print("\n\nShortest Possible Path (After backtracking):")   #Only up, down, left, right movements allowed. Solution Path.
        # shortest_path = []
        # while state is not None:
        #     shortest_path.append(state)
        #     state = state.parent
        # shortest_path.reverse()
        # for index, s in enumerate(shortest_path):
        #     print(f"Move {index}:\n{s}\n")

        print(f"\nGreedyBFS traversal Steps to reach Goal: {len(path) - 1}")
        print(f"Total Nodes Expanded (Search Effort): {nodes_expanded}")
        print(f"Total cost: {cost}")
    ##-------
    
    #Main
    def solve(self):
        try:
            counter = itertools.count()   
            heap = [(self.initial_cost, next(counter), self.starting_state)]
            visited = {self.starting_state}
            nodes_expanded = 0
            current_path_cost = 0
            current_path = []

            while heap:
                cost, _, obj = heapq.heappop(heap)   # notice the "_"
                current_path.append(obj)
                current_path_cost += cost
                visited.add(obj)

                nodes_expanded += 1

                if obj.board == self.goal_board:
                    print("✅ Goal reached using GBFS!\n")
                    self.show_stats(obj, current_path, current_path_cost, nodes_expanded)
                    return

                for a, b in obj.get_neighbours():
                    if b not in visited:
                        heapq.heappush(heap, (a, next(counter), b))  # 3-tuple

            print("❌ No solution found with GreedyBFS.")
        
        except Exception as e:
            raise RuntimeError(f"Solver failed due to error: {e}")





if __name__ == "__main__":
    #Example Run
    starting_board = [[1, 2, 3],
                      [5, 6, 0],
                      [7, 8, 4]]

    goal_board = [[1, 2, 3],
                  [5, 8, 6],
                  [0, 7, 4]]

    puzzle1 = PuzzleSolverGreedyBFS(starting_board, goal_board)
    puzzle1.solve()


        
    
        
