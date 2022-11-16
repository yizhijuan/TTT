# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


class Game:
    def __init__(self):
        self.winner = None
    def other_player(self,type):
        """Given the character for a player, returns the other player."""
        if type == 'O':
            type = 'X'
        else:
            type = 'O'
        return type
    def get_winner(self,board,type):
        for key in('O','X'):
            for i in range(3):
                if board.board[i][0] == key and board.board[i][1] == key and board.board[i][2] == key:
                    self.winner = key
                    break
                elif board.board[0][i] == key and board.board[1][i] == key and board.board[2][i] == key:
                    self.winner = key
                    break  
            if (board.board[0][0] == key and board.board[1][1] == key and board.board[2][2] == key) or (board.board[0][2] == key and board.board[1][1] == key and board.board[2][0] == key):
                self.winner = key
        if self.winner != None:
            print(self.winner, "wins!")
        else:
            print("This is", self.other_player(type), "'s turn")
        print("\n") 

