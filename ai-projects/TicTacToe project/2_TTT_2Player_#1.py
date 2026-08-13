# Written by self. Error Handling Included.


import random

class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        # for row in range(3):
        #     row = []
        #     for i in range(3):
        #         row.append('-')
        #     self.board.append(row)
        self.board = [['-' for _ in range(3)] for _ in range(3)]
        
    def show_board(self):
        for row in self.board:
            row = " ".join(row)
            print(row)
    
    def select_first_turn(self):
        return random.randint(0, 1)
    
    def fix_spot(self, row, col, player_turn):
        self.board[row-1][col-1] = player_turn

    def swap_player_turn(self, player_turn):
        return 'X' if player_turn == 'O' else 'O'

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_player_win(self, player_turn):
         
        win = None
        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player_turn:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player_turn:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player_turn:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player_turn:
                win = False
                break
        if win:
            return win

        return False



    #Main Function
    def start(self):

        while True:  #For Playing Again and Again

            self.create_board()
            player_turn = 'X' if self.select_first_turn() == 1 else 'O'
            print(f"New Game:\nTossing...\n{player_turn} Wins!")

            while True:
                print(f"\nPlayer {player_turn} Turn:")
                self.show_board()
                try:
                    row, col = list(map(int, input("Enter row and column numbers to fix spot: ").split()))
                except:
                    print("Invalid Input")
                    a = input("Press Enter to continue the game: ")
                    if a == "exit":
                        return
                    continue
                print()

                #Preventing replacement
                if self.board[row-1][col-1] == '-':
                    self.fix_spot(row, col, player_turn)
                else:
                    print("Spot already filled")
                    continue
                
                #Case 1: A player wins
                if self.is_player_win(player_turn):
                    self.show_board()
                    print(f"Player {player_turn} Wins!")
                    break

                #Case 2: The board is filled before a player wins
                if self.is_board_filled():
                    print("It's a Tie!")    
                    break   #Breaking out of the bigger loop.
                
                player_turn = self.swap_player_turn(player_turn)


            again = input("\nPress Enter to play again.\nEnter anything else to exit program.")
            if again!="":
                print("----------\n")
                break



# starting the game
game1 = TicTacToe()

if __name__ == "__main__":
    game1.start()