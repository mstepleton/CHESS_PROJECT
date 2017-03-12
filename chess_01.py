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
        print('White Graveyard: ', self.white_graveyard)
        print('Black Graveyard: ', self.black_graveyard)

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
        if p.check_move(b, dest) == True:
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
        if dest[0] - self.square[0] == 1 and abs(self.square[1] - dest[1]) == 0:
            if b.board[dest] == '..':
                return 'Empty'
            elif self.name[0].isupper == b.board[dest][0].isupper:
                return 'Occupied'
            elif self.name[0].isupper != b.board[dest][0].isupper:
                return 'Take'
            else:
                return 'Error'
        else:
            return 'Invalid Move'

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
        self.game = True
        self.P0 = Pawn(b=self.board, team='white', square=(1, 0), name='P0')
        self.p0 = Pawn(b=self.board, team='black', square=(6, 0), name='p0')


    def move(self, b, p, dest):
        if p.check_move(b, dest) == 'Empty':
            b.board[p.square] = '..'
            b.board[dest] = p.name
            p.square = dest
        if p.check_move(b, dest) == 'Take':
            if b.board[dest].isupper:
                self.board.white_graveyard.append(b.board[dest])
            else:
                self.board.black_graveyard.append(b.board[dest])
            b.board[p.square] = '..'
            b.board[dest] = p.name
            p.square = dest
            print('Piece Taken!')
        if p.check_move(b, dest) == 'Invalid Move':
            print('Invalid Move!')

    def play(self):
        print('Game Starting!')
        while self.game:
            g.board.print_board()
            print('Time to make a move!')
            piece_input = input('Choose a piece: ')
            dest_row = int(input('Choose row destination'))
            dest_column = int(input('Choose column destination'))
            dest_input = (dest_row, dest_column)
            g.move(b=g.board, p=eval('g.'+piece_input), dest=dest_input)
            print('move over!')
            continue







g = Game()
g.play()




