# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

import random
from logic import make_empty_board
from logic import get_winner
from logic import other_player

if __name__ == '__main__':
    board = make_empty_board()
    '''
    board = [['O', 'X', 'X'],
            ['X', 'X', 'O'],
            ['O', 'X', 'X']]
    '''
    winner = None
    # a single player or 2 players
    print("Please enter the number of player(s):")
    player_number = int(input())
    if player_number == 1:
        is_player_turn = 1
        while winner == None:
            if is_player_turn == 1:
                print("TODO: take a turn!")
                # TODO: Show the board to the user.
                for i in range(3):
                    print(board[i])
                # TODO: Input a move from the player.
                position = int(input())
                x = position / 3 - 1
                y = (position + 2 ) % 3
                chess = 'X'
                is_player_turn = 0
            elif is_player_turn == 0:
                # bot generates a position
                while board[x][y] != None:
                    position = random.randint(0,10)
                    x = position / 3 - 1
                    y = (position + 2 ) % 3
                # TODO: Update the board.
                board[x][y] = 'O'
                for i in range(3):
                    print(board[i])
                winner = get_winner(board)
                # TODO: Update who's turn it is.
                if winner != None:
                    print(winner, "wins!")
                else:
                    print("This is", other_player(chess), "'s turn")
                print("\n")
    
    if player_number == 2:
        while winner == None:
            print("TODO: take a turn!")
            # TODO: Show the board to the user.
            for i in range(3):
                print(board[i])
            # TODO: Input a move from the player.
            position = int(input())
            x = position / 3 - 1
            y = (position + 2 ) % 3
            chess = input()
            # TODO: Update the board.
            board[x][y] = chess
            for i in range(3):
                print(board[i])
            winner = get_winner(board)
            # # TODO: Update who's turn it is.
            if winner != None:
                print(winner, "wins!")
            else:
                print("This is", other_player(chess), "'s turn")
            print("\n")