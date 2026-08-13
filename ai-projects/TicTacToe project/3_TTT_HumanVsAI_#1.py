# Using NumPy arrays, tuples and sets for efficiency.
# Human Vs AI 



#ON HOLD for now: Will revisit this later.



import numpy as np
import random

class TicTacToeAI:
    def __init__(self):
        self.board = np.full((3, 3), '-')  # 3x3 board with '-'

    def show_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def is_winner(self, player):
        # rows, cols, diagonals
        return (
            any(np.all(self.board[i, :] == player) for i in range(3)) or
            any(np.all(self.board[:, j] == player) for j in range(3)) or
            np.all(np.diag(self.board) == player) or
            np.all(np.diag(np.fliplr(self.board)) == player)
        )

    def is_full(self):
        return not np.any(self.board == '-')

    def available_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i, j] == '-']

    def minimax(self, is_maximizing):
        if self.is_winner('O'): return 1
        if self.is_winner('X'): return -1
        if self.is_full(): return 0

        if is_maximizing:  # AI's turn
            best_score = -float('inf')
            for (i, j) in self.available_moves():
                self.board[i, j] = 'O'
                score = self.minimax(False)
                self.board[i, j] = '-'
                best_score = max(best_score, score)
            return best_score
        else:  # Human's turn
            best_score = float('inf')
            for (i, j) in self.available_moves():
                self.board[i, j] = 'X'
                score = self.minimax(True)
                self.board[i, j] = '-'
                best_score = min(best_score, score)
            return best_score

    def best_move(self):
        best_score = -float('inf')
        move = None
        for (i, j) in self.available_moves():
            self.board[i, j] = 'O'
            score = self.minimax(False)
            self.board[i, j] = '-'
            if score > best_score:
                best_score = score
                move = (i, j)
        return move

    def play(self):
        print("Welcome to Human vs AI TicTacToe!\n")
        self.show_board()

        while True:
            # Human move
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

            self.show_board()
            if self.is_winner('X'):
                print("🎉 Human wins!")
                break
            if self.is_full():
                print("It's a draw!")
                break

            # AI move
            print("AI is thinking...")
            move = self.best_move()
            self.board[move] = 'O'

            self.show_board()
            if self.is_winner('O'):
                print("🤖 AI wins!")
                break
            if self.is_full():
                print("It's a draw!")
                break


# Run the game
game = TicTacToeAI()
game.play()
