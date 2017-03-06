class Board:
    """ This class is for the board.  It will:
        - Build the board when the game is initiall started
        - Store game states between and during turns
            - FEN state functionality
        - have functions that show available moves for each piece
        - have function to print the board nicely
    """

    def __init__(self):
        self.row = [0, 1, 2, 3, 4, 5, 6, 7]
        self.column = [0, 1, 2, 3, 4, 5, 6, 7]
        self.board = [(a, b) for a in self.row for b in self.column]

    def print_board(self):
        for i in self.board:
            print(i)


class Piece:
    """ This class is the super class for all pieces. It will store information and attributes common to all pieces:
        - Whether the piece is still on the board.
        - not sure - probably more things
    """

    def __init__(self, team):
        self.team = team

    def move(self, dest):
        self.square = dest
        return self.square

class King(Piece):
    """ This is the White King piece class.  It will store information about this piece.
        - Whether this piece is on the board
        - What this piece's location is
        - This piece's moveset
        -
    """

    def __init__(self, team, square):
        Piece.__init__(self, team)
        self.square = square


class Game:
    """ This class controls the flow of the game and the decision-making of the AI.  Also:
        - Function to check for game state (mate, etc.)
        - Function to check for
    """
    def __init__(self):
        self.board = Board()
        self.wking = King(team = 'W', square = (7, 3))


g = Engine()
b = g.board
b.print_board()
wk = g.wking
print(wk.square)
wk.move(dest = (8,4))
print(wk.square)

