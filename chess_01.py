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
        self.squares = [(a, b) for a in self.row for b in self.column]
        self.board = dict((key, '.') for key in self.squares)



    def print_board(self):
        for i in range(8)[::-1]:
            row = ''
            for j in range(8):
               row += ' ' + self.board[(i,j)]
            print(row)

    def check_pieces(self):
        pass


    def move_piece(self, piece, dest):
        pass


class Piece:
    """ This class is the super class for all pieces. It will store information and attributes common to all pieces:
        - Whether the piece is still on the board.
        - not sure - probably more things
    """

    def __init__(self, team, square):
        self.team = team
        self.square = square



class King(Piece):
    """ This is the White King piece class.  It will store information about this piece.
        - Whether this piece is on the board
        - What this piece's location is
        - This piece's moveset
        -
    """
    KingList = []

    def __init__(self):
        Piece.__init__(self, team, square)
        self.KingList.append(team)

    """
    def check_move(self, square, dest):
        if abs(square[0] - dest[0]) <= 1 and abs(square[1] - dest[1]) <= 1:
            pass
    """

    def move(self, dest):
        self.square = dest
        return self.square


class Game:
    """ This class controls the flow of the game and the decision-making of the AI.  Also:
        - Function to check for game state (mate, etc.)
        - Function to check for
    """
    def __init__(self):
        self.board = Board()
        WhiteKing = King(self, team='white', square = (0, 4))


g = Game()
b = g.board
b.print_board()



