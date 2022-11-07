# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

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
    while winner == None:
        print("TODO: take a turn!")
        # TODO: Show the board to the user.
        for i in range(3):
            print(board[i])
        # TODO: Input a move from the player.
        x = int(input())
        y = int(input())
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