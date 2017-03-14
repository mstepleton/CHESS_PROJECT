from itertools import cycle

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

    # Inheritable Piece of possible_moves
    def available_spaces(self, b, p):
        self.move_set = {}
        for i in b.board.keys():
            if b.board[i] == '..':
                self.move_set[i] = 'Empty'
            elif b.board[i].isupper() != p.name.isupper():
                self.move_set[i] = 'Enemy'
        return self.move_set


class Pawn(Piece):

    def __init__(self, b, team, square, name):
        self.team = team
        self.square = square
        self.name = name
        self.moved = False
        self.possible_moves = {}
        self.available_moves = {}
        Piece.__init__(self)
        b.board[square] = self.name

    def move_search(self, b, p):
        self.available_moves = Piece.available_spaces(self, b, p)
        print(self.available_moves)
        if self.moved == False:
            for i in self.available_moves.keys():
                if self.team == 'White':
                    if 0 < i[0] - self.square[0] <= 2 and self.square[1] - i[1] == 0 and self.available_moves[i] == 'Empty':
                        self.possible_moves[i] = 'Empty'
                    elif self.square[0] - i[0] == 1 and abs(self.square[1] - i[1] == 1) and self.availabe_moves[i] == 'Enemy':
                        self.possible_moves[i] = 'Enemy'
                elif self.team == 'Black':
                    if 0 < self.square[0] - i[0] <= 2 and self.square[1] - i[1] == 0 and self.available_moves[i] == 'Empty':
                        self.possible_moves[i] = 'Empty'
                    elif self.square[0] - i[0] == 1 and abs(self.square[1] - i[1] == 1) and self.availabe_moves[i] == 'Enemy':
                        self.possible_moves[i] = 'Enemy'
        elif self.moved == True:
            for i in self.available_moves.keys():
                if self.team == 'White':
                    if i[0] - self.square[0] == 1 and self.square[1] - i[1] == 0 and self.available_moves[i] == 'Empty':
                        self.possible_moves[i] = 'Empty'
                    elif self.square[0] - i[0] == 1 and abs(self.square[1] - i[1] == 1) and self.availabe_moves[i] == 'Enemy':
                        self.possible_moves[i] = 'Enemy'
                elif self.team == 'Black':
                    if self.square[0] - i[0] == 1 and self.square[1] - i[1] == 0 and self.available_moves[i] == 'Empty':
                        self.possible_moves[i] = 'Empty'
                    elif self.square[0] - i[0] == 1 and abs(self.square[1] - i[1] == 1) and self.availabe_moves[i] == 'Enemy':
                        self.possible_moves[i] = 'Enemy'
        return self.possible_moves

class Knight(Piece):

    def __init__(self, b, team, square, name):
        self.team = team
        self.square = square
        self.name = name
        self.moved = False
        self.possible_moves = {}
        self.available_moves = {}
        Piece.__init__(self)
        b.board[square] = self.name

    def move_search(self, b, p):
        self.available_moves = Piece.available_spaces(self, b, p)

        return self.possible_moves

class Bishop(Piece):

    def __init__(self, b, team, square, name):
        self.team = team
        self.square = square
        self.name = name
        self.moved = False
        self.possible_moves = {}
        self.available_moves = {}
        Piece.__init__(self)
        b.board[square] = self.name

    def move_search(self, b, p):
        self.available_moves = Piece.available_spaces(self, b, p)

        return self.possible_moves


class Rook(Piece):

    def __init__(self, b, team, square, name):
        self.team = team
        self.square = square
        self.name = name
        self.moved = False
        self.possible_moves = {}
        self.available_moves = {}
        Piece.__init__(self)
        b.board[square] = self.name

    def move_search(self, b, p):
        self.available_moves = Piece.available_spaces(self, b, p)

        return self.possible_moves


class King(Piece):

    def __init__(self, b, team, square, name):
        self.team = team
        self.square = square
        self.name = name
        self.moved = False
        self.possible_moves = {}
        self.available_moves = {}
        Piece.__init__(self)
        b.board[square] = self.name

    def move_search(self, b, p):
        self.available_moves = Piece.available_spaces(self, b, p)

        return self.possible_moves


class Queen(Piece):

    def __init__(self, b, team, square, name):
        self.team = team
        self.square = square
        self.name = name
        self.moved = False
        self.possible_moves = {}
        self.available_moves = {}
        Piece.__init__(self)
        b.board[square] = self.name

    def move_search(self, b, p):
        self.available_moves = Piece.available_spaces(self, b, p)

        return self.possible_moves
class Game:
    """ This class controls the flow of the game and the decision-making of the AI.  Also:
        - Function to check for game state (mate, etc.)
        - Function to check for
    """
    def __init__(self):
        self.board = Board()
        self.game = True
        self.turn = True
        self.teams =cycle(['White', 'Black'])
        self.P0 = Pawn(b=self.board, team='White', square=(1, 0), name='P0')
        self.p0 = Pawn(b=self.board, team='Black', square=(6, 0), name='p0')
        self.p1 = Pawn(b=self.board, team='Black', square=(2, 1), name='p1')
        self.P1 = Pawn(b=self.board, team='White', square=(1, 1), name='P1')
    def move(self, b, p, dest):


        if p.check_move(b, dest) == 'Empty':
            b.board[p.square] = '..'
            b.board[dest] = p.name
            p.square = dest
        elif p.check_move(b, dest) == 'Take':
            if b.board[dest].isupper:
                self.board.white_graveyard.append(b.board[dest])
            else:
                self.board.black_graveyard.append(b.board[dest])
            b.board[p.square] = '..'
            b.board[dest] = p.name
            p.square = dest
            print('Piece Taken!')
        elif p.check_move(b, dest) == 'Invalid Move':
            print('Invalid Move!')

    def play(self, b):
        print('Game Starting!')
        while self.game == True:
            self.team_turn = next(self.teams)
            while self.turn == True:
                g.board.print_board()
                print('Turn: '+self.team_turn)
                while True:
                    piece_input = input('Choose a piece: ')
                    dest_input = str(input('Choose a destination square: '))
                    if eval('g.'+piece_input).check_move(b, eval(dest_input)) == 'Invalid Move':
                        print('Invalid square.  Please try again.')
                    else:
                        g.move(b=g.board, p=eval('g.'+piece_input), dest=eval(dest_input))
                        break
                print('move over!')
                break







g = Game()
g.board.print_board()
print(g.P0.move_search(g.board, g.P0))





