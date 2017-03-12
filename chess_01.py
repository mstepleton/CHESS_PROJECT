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
        self.board = dict((key, '..') for key in self.squares)
        self.white_graveyard = []
        self.black_graveyard = []

    def print_board(self):
        for i in range(8)[::-1]:
            row = ''
            for j in range(8):
               row += ' ' + self.board[(i,j)]
            print(row)

    def add_piece(self, p):
        self.board[p.square] = p.name

    def drop_piece(self, p):
        self.board[p.square] = '..'


class Piece:
    """ This class is the super class for all pieces. It will store information and attributes common to all pieces:
        - Whether the piece is still on the board.
        - not sure - probably more things
    """
    def __init__(self, status = True):
       self.status = status
       pass

    def move(self, b, p, dest):
        if p.check_move(dest) == True:
            b.board[dest] = p.name


class Pawn(Piece):
    """ This is the White King piece class.  It will store information about this piece.
        - Whether this piece is on the board
        - What this piece's location is
        - This piece's moveset
        -
    """
    PawnList = []

    def __init__(self, b, team, square, name):
        self.team = team
        self.square = square
        self.name = name
        Piece.__init__(self)
        b.board[square] = self.name

    def check_move(self, b, dest):
        if abs(self.square[0] - dest[0]) <= 1 and abs(self.square[1] - dest[1]) == 0:
            if b.board[(dest)] == '..':
                return 'Empty'
            elif b.board[(dest])[0].isupper:
        if
        else:
            return False

class King(Piece):
    """ This is the White King piece class.  It will store information about this piece.
        - Whether this piece is on the board
        - What this piece's location is
        - This piece's moveset
        -
    """
    KingList = []

    def __init__(self, team, square, name):
        self.team = team
        self.square = square
        self.name = name
        Piece.__init__(self)
        self.KingList.append(team)

    def check_move(self, square, dest):
        if abs(square[0] - dest[0]) <= 1 and abs(square[1] - dest[1]) <= 1:
            pass




class Game:
    """ This class controls the flow of the game and the decision-making of the AI.  Also:
        - Function to check for game state (mate, etc.)
        - Function to check for
    """
    def __init__(self):
        self.board = Board()
        self.P0 = Pawn(b=self.board, team='white', square=(1, 0), name='P0')

        """
        P1 = Pawn(team='white', square=(1, 1), name = 'P1')
        P2 = Pawn(team='white', square=(1, 2), name = 'P2')
        P3 = Pawn(team='white', square=(1, 3), name = 'P3')
        P4 = Pawn(team='white', square=(1, 4), name = 'P4')
        P5 = Pawn(team='white', square=(1, 5), name = 'P5')
        P6 = Pawn(team='white', square=(1, 6), name = 'P6')
        P7 = Pawn(team='white', square=(1, 7), name = 'P7')
        R1 = King(team='white', square=(0, 0), name='R1')
        K1 = King(team='white', square=(0, 1), name = 'K1')
        B1 = King(team='white', square=(0, 2), name='B1')
        QQ = King(team='white', square=(0, 3), name='QQ')
        KK = King(team='white', square=(0, 4), name='KK')
        B2 = King(team='white', square=(0, 5), name='B2')
        K2 = King(team='white', square=(0, 6), name='K2')
        R2 = King(team='white', square=(0, 7), name='R2')
        self.board.add_piece(self.P0)
        self.board.add_piece(P1)
        self.board.add_piece(P2)
        self.board.add_piece(P3)
        self.board.add_piece(P4)
        self.board.add_piece(P5)
        self.board.add_piece(P6)
        self.board.add_piece(P7)
        self.board.add_piece(R1)
        self.board.add_piece(K1)
        self.board.add_piece(B1)
        self.board.add_piece(QQ)
        self.board.add_piece(KK)
        self.board.add_piece(B2)
        self.board.add_piece(K2)
        self.board.add_piece(R2)
"""

    def move(self, b, p, dest):
        if p.check_move(dest) == True:
            b.board[p.square] = '..'
            b.board[dest] = p.name



g = Game()
g.board.print_board()
print(g.P0.check_move((2,0)))
g.move(g.board, g.P0, (2, 0))
print('--------')

g.board.print_board()




