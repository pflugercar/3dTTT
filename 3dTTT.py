#   3d Tic Tack Toe (3dTTT)
#   by Craig Reinecke
#   craig@rhino-key.com

import numpy as np

class PlayerInfo:
    def __init__(self):
        # Default is 3 players.
        self.numPlayers = 3

        # These are just for initialization
        p1name = "Player 1"
        p2name = "Player 2"
        p3name = "Player 3"
        p1 = "X"
        p2 = "O"
        p3 = "Z"

        # These are accessible in the code
        self.whosTurn = 1
        self.lineupNames = [p1name, p2name,p3name]
        self.lineupPieces = [p1, p2, p3]


# Setting up the board
class Game:
    def __init__(self):
        blank = "░"
        core =  "█"        
        self.size = 3
        self.board = np.array(
            [[[blank,blank,blank],[blank,blank,blank],[blank,blank,blank]],
            
            [[blank,blank,blank],[blank,core,blank],[blank,blank,blank]],
            
            [[blank,blank,blank],[blank,blank,blank],[blank,blank,blank]]])



# Menu for players to update their game settings
def mainMenu(numPlayers, board):
    print(numPlayers)


# print out the board
def printBoard(board):
    # testing menu choices here
    top = ["(1)", "(2)", "(3)"]
    row = ["(1)", "(2)", "(3)"]
    col = ["(1)", "(2)", "(3)"]
    
    print(f"       {top[0]} Top                {top[1]} Middle             {top[2]} Bottom\n")
    print(f"    ", end="")
    for num in range(3):
        print(f" {col[0]}   {col[1]}   {col[2]}        ", end="")
    print("")

    for numrow in range(board.size):

        for nlayer in range(board.size):
            print(f" {row[numrow]}  ", end="")
            for element in range(board.size):
                if (element == board.size - 1):
                    spacer = "   "
                else:
                    spacer = " │ "
                print(board.board[numrow,nlayer,element], end=' {} '.format(spacer))

            if numrow != 2 & nlayer == 2:
                print("\n    ─────┼─────┼─────       ─────┼─────┼─────       ─────┼─────┼─────")

    # Adding new line plus one blank line 
    print("\n\n")


# End game menu to optionally play again.
def endGameMenu():
    stillplaying = True
    again = input("Play again?  y/n: ")
    if(again == "n"):
        stillplaying = False
        print("game over")

    return stillplaying


# Beginning of the whole game
players = PlayerInfo()
board = Game()

mainMenu(players.numPlayers, board)

playing = True
while playing:
    # clearing the screen
    print(chr(27) + "[2J")
    
    message = players.lineupNames[0] + ", what is your move? "
 
    validMove = False
    while not validMove:
        printBoard(board)
# For testing
#        choice = input(message)
#        if choice == "y":
#            validMove = True
        validMove = True

    # End menu allows players to quit, or keep or change 
    # game settings if they are still playing.
    #playing = endGameMenu()
    playing = False;

print("Goodbye, world!")
