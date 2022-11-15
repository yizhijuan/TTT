# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

import random
from logic import make_empty_board
from logic import get_winner
from logic import other_player


class Board:
    def __init__(self):
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
    def print_board(self):
        for i in range(3):
            print(self.board[i])
    def is_valid_move(self, position):
        x = (position + 2) // 3 - 1
        y = (position + 2 ) % 3
        if self.board[x][y] == None:
            return True
        else:
            return False
    def change_board(self, position, type):
        if self.is_valid_move(position):
            x = (position + 2) // 3 - 1
            y = (position + 2 ) % 3
            self.board[x][y] = type
            return self.board


if __name__ == '__main__':
    board = Board()
    winner = None
    # a single player or 2 players
    print("Please enter the number of human player:")
    player_number = int(input())
    board.print_board()
    if player_number == 1:
        is_player1_turn = 1
        print("This is X's turn")
        while winner == None:
            if is_player1_turn == 1:
                # Input a move from the player.
                print("Please enter the position(1~9)")
                position = int(input())
                type = 'X'
                is_player1_turn = 0
            elif is_player1_turn == 0:
                # Bot generates a position
                while board.is_valid_move(position) == False:
                    position = random.randint(0,10)                  
                type = 'O'  
                is_player1_turn = 1
            # Update the board.
            board.change_board(position, type) 
            board.print_board()
            winner = get_winner(board)
            # Update who's turn it is.
            if winner != None:
                print(winner, "wins!")
            else:
                print("This is", other_player(type), "'s turn")
            print("\n")
    
    if player_number == 2:
        is_player1_turn = 1
        while winner == None:
            print("Please enter the position(1~9)")
            if is_player1_turn == 1:
                # Input a move from the player1.
                position = int(input())
                type = 'X'
                is_player1_turn = 0
            elif is_player1_turn == 0:
                # Input a move from the player2.
                position = int(input())                  
                type = 'O'  
                is_player1_turn = 1
            # Update the board.
            board.change_board(position, type) 
            board.print_board()
            winner = get_winner(board)
            # Update who's turn it is.
            if winner != None:
                print(winner, "wins!")
            else:
                print("This is", other_player(type), "'s turn")
            print("\n")  
