# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.
from pd import games_pd


class Game:
    def __init__(self):
        self.winner = None
        self.turn = 0 #轮次数
        self.player1_name = None
        self.player2_name = None
    def pre_set(self, board, player_number):
        if player_number == 1:
            is_player1_turn = 1
            print("Enter player's name:")
            self.player1_name = str(input())
            self.player2_name = 'Bot'
        elif player_number == 2:
            is_player1_turn = 1
            print("Enter player1's name:")
            self.player1_name = str(input())
            print("Enter player2's name:")
            self.player2_name = str(input())
        board.print_board()
        print("This is X's turn")
        return is_player1_turn

    def add_game(self, games_pd, player1_name, player2_name, winner):   
        games_pd.loc[len(games_pd)] = {
            "Game ID":len(games_pd) + 1,
            "Player1":player1_name,
            "Player2":player2_name,
            "Winner":winner
        }
        return games_pd
    #append?    

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
        if self.winner == 'O':
            print(self.player2_name, "wins!")
            return self.player2_name
        elif self.winner == 'X':
            print(self.player1_name, "wins!")
            return self.player1_name
        else:
            print("This is", self.other_player(type), "'s turn")
        print("\n") 
        return self.winner
