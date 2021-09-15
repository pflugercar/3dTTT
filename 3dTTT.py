#   3d Tic Tack Toe (3dTTT)
#   by Craig Reinecke
#   craig@rhino-key.com


# Setup global variables
class PlayerInfo:
    def __init__(self):
        self.numPlayers = 3
        p1name = "player 1"
        p2name = "player 2"
        p3name = "player 3"
        p1 = "X"
        p2 = "O"
        p3 = "Z"


# Setting up the board
class Game:
    def __init__(self):
        layer = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        self.board = [layer, layer, layer]
        self.whosTurn = 1


# Menu for players to update their game settings
def mainMenu(numPlayers, board):
    print(numPlayers)


# print out the board
def printBoard(board):
    pass


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
    printBoard(board)

    # End menu allows players to quit, or keep or change 
    # game settings if they are still playing.
    playing = endGameMenu()
