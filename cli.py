# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

import random
from logic import Game
from pd import moves
from pd import games_pd

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
    game = Game()
    game.winner = None
    # a single player or 2 players
    print("Please enter the number of human player:")
    player_number = int(input())
    (is_player1_turn, player1_name, player2_name) = game.pre_set(board, player_number)
        
    while game.winner == None:
        if is_player1_turn == 1:
            # Input a move from the player.
            print("Please enter the position(1~9)")
            position = int(input())
            type = 'X'
            is_player1_turn = 0
        elif is_player1_turn == 0:
            # Bot generates a position
            if player_number == 1:
                while board.is_valid_move(position) == False:
                    position = random.randint(1,9)                  
            elif player_number == 2:
                position = int(input()) 
            type = 'O'  
            is_player1_turn = 1
        # Update the board.
        board.change_board(position, type) 
        board.print_board()
        game.get_winner(board,type)
        game.add_game(player1_name,player2_name,game.winner)

        if is_player1_turn == 1:
            moves.loc[len(moves)] = {
                "Game ID":len(games_pd),
                "Turn":0,
                "Player":player1_name,
                "Position":position
            }
        elif is_player1_turn == 0:
            moves.loc[len(moves)] = {
                "Game ID":len(games_pd),
                "Turn":0,
                "Player":player2_name,
                "Position":position
            }

    games_pd.to_csv("games_pd.csv")
    moves.to_csv("moves.csv")

    exit()