#   3d Tic Tack Toe (3dTTT)
#   by Craig Reinecke and Ramon Morales
#   craig@rhino-key.com

import numpy as np

class PlayerInfo:
    def __init__(self):
        # Default is 3 players.
        self.num_players = 3

        # These are just for initialization
        name1 = "Player 1"
        name2 = "Player 2"
        name3 = "Player 3"
        piece1 = "X"
        piece2 = "O"
        piece3 = "Z"

        # These are accessible in the code
        self.whos_turn = 1
        self.lineup_names = [name1, name2, name3]
        self.lineup_pieces = [piece1, piece2, piece3]

    def rotate_players(self):
        self.lineup_names.append(self.lineup_names[0])
        self.lineup_names.pop(0)
        self.lineup_pieces.append(self.lineup_pieces[0])
        self.lineup_pieces.pop(0)
        if self.whos_turn == self.num_players:
            self.whos_turn = 1
        else:
            self.whos_turn += 1


# Setting up the board
class GameClass:

    def __init__(self):
        #temporary variables for setting the board
        blank = "░"
        core =  "█"
        self.size = 3

        # The board layout has a blank core in the center
        self.board = np.array(
            [[[blank,blank,blank], [blank,blank,blank], [blank,blank,blank]],
            
            [[blank,blank,blank], [blank,core,blank], [blank,blank,blank]],
            
            [[blank,blank,blank], [blank,blank,blank], [blank,blank,blank]]])

        # choice_level is the indice for the last_moves. Also controls menu display.
        self.choice_level = 0
        self.last_moves = [None, None, None]

    # Returns True/False if the last_moves is available.
    # For testing purposes, it only returns True.
    def check_valid(self):
        self.last_moves[self.choice_level] = int(self.last_moves[self.choice_level])
        return True

    # Check if the last move is a winning move.
    def is_winner(self):
        return False


# Menu for players to update their game settings
def main_menu(num_players, game):
    pass


# print out the board
def print_board(game):

    # clearing the screen
    print(chr(27) + "[2J")
    
    # prepping to either display or hide user board selection choices.
    if game.choice_level == 0:
        top = ["(1)", "(2)", "(3)", "(1)", "(2)", "(3)"]
    else:
        top = ["   ", "   ", "   ", "   ", "   ", "   "]
        top[game.last_moves[0] - 1] = "-->"
        top[game.last_moves[0] - 1 + 3] = "<--"

    row = np.array([["   ", "   ", "   "],["   ", "   ", "   "],["   ", "   ", "   "]])
    if game.choice_level >= 1:
        if game.choice_level == 1:
            row[game.last_moves[0] - 1] = ["(1)", "(2)", "(3)"]
        else:
            row[game.last_moves[0] - 1] [game.last_moves[1] - 1] = "-->"
            
#        for x in range(len(row_menu)):
#            row[game.last_moves[0]] [x] = row_menu[x]

    col = ["   ", "   ", "   "]
    if game.choice_level == 2:
        col = ["(1)", "(2)", "(3)"]


    # printing the layer header
    print(f"       {top[0]} Top {top[3]}            {top[1]} Middle {top[4]}         {top[2]} Bottom {top[5]}\n")

    # spacer for the beginning of the column selection
    column_header = f"    "
    # print column headers if needed
    if game.choice_level >= 1:
        col_shift_amount = game.last_moves[0] - 1
        # 24 spaces used to push over the column selection
        column_header += col_shift_amount * "                        "
        column_header += f" {col[0]}   {col[1]}   {col[2]}        "
    print(column_header)

    # prints the board from a top down view
    b = np.ndarray.copy(game.board)
    print(f"""\
 {row[0][0]}  {b[0][0][0]}  │  {b[0][0][1]}  │  {b[0][0][2]}     \
 {row[1][0]}  {b[1][0][0]}  │  {b[1][0][1]}  │  {b[1][0][2]}     \
 {row[2][0]}  {b[2][0][0]}  │  {b[2][0][1]}  │  {b[2][0][2]}
    ─────┼─────┼─────       ─────┼─────┼─────       ─────┼─────┼─────
 {row[0][1]}  {b[0][1][0]}  │  {b[0][1][1]}  │  {b[0][1][2]}     \
 {row[1][1]}  {b[1][1][0]}  │  {b[1][1][1]}  │  {b[1][1][2]}     \
 {row[2][1]}  {b[2][1][0]}  │  {b[2][1][1]}  │  {b[2][1][2]}
    ─────┼─────┼─────       ─────┼─────┼─────       ─────┼─────┼─────
 {row[0][2]}  {b[0][2][0]}  │  {b[0][2][1]}  │  {b[0][2][2]}     \
 {row[1][2]}  {b[1][2][0]}  │  {b[1][2][1]}  │  {b[1][2][2]}     \
 {row[2][2]}  {b[2][2][0]}  │  {b[2][2][1]}  │  {b[2][2][2]}""")
    print("\n\n")


# End game menu to optionally play again.
def endGameMenu(status):
    return True
    stillplaying = True
    again = input("Play again?  y/n: ")
    if(again == "n"):
        stillplaying = False
        print("game over")

    return stillplaying


# This is a function to print game data for debugging
def printGameInfo(game):
    print("\nChoice Level =", game.choice_level)
    print("Last Moves   =", game.last_moves)

# Beginning of the whole game
players = PlayerInfo()
game = GameClass()

main_menu(players.num_players, game)

playing = True
while playing:

    message = players.lineup_names[0] + ", what is your move?  "
    
    while playing and game.choice_level != 3:
        print_board(game)
        game.last_moves[game.choice_level] = input(message)
        if game.check_valid():
            printGameInfo(game)
            game.choice_level += 1
    
    

    # store choices in the game board and checks for winner
    game.board[game.last_moves[0] - 1] [game.last_moves[1] - 1] [game.last_moves[2] - 1] = players.lineup_pieces[0]
    status = game.is_winner()
    
    if status:
        # Celebrate!!!  write code here
        endGameMenu
        break

    # reset and rotate players
    game.choice_level = 0
    game.last_moves = [None, None, None]
    players.rotate_players()

    # End menu allows players to quit, or keep or change 
    # game settings if they are still playing.    

print("Yay, the game has ended!!")
