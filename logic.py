# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    win = 0 #no one wins
    for key in('O','X'):
        for i in range(3):
            if board.board[i][0] == key and board.board[i][1] == key and board.board[i][2] == key:
                win = 1
                winner = key
                break
            elif board.board[0][i] == key and board.board[1][i] == key and board.board[2][i] == key:
                win = 1
                winner = key
                break
            
        if (board.board[0][0] == key and board.board[1][1] == key and board.board[2][2] == key) or (board.board[0][2] == key and board.board[1][1] == key and board.board[2][0] == key):
            win = 1
            winner = key
    if win == 0:
        winner = None  
    return winner


def other_player(player):
    """Given the character for a player, returns the other player."""
    if player == 'O':
        player = 'X'
    else:
        player = 'O'
    return player