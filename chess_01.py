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



class Pawn(Piece):

    def __init__(self, b, team, square, name):
        self.team = team
        self.square = square
        self.name = name
        self.moved = False
        self.move_set = self.move_set_adjust([(1, 0), (2, 0)])
        self.move_set_enemy = self.move_set_adjust([(1, -1), (1, 1)])
        self.possible_moves = self.move_search(b)
        b.board[square] = self.name

    def move_set_adjust(self, move_set):
        if self.team == 'Black':
            move_set = [(i[0] * -1, i[1]) for i in move_set]
        return move_set

    def move_search(self, b):
        self.possible_moves = {}
        # Open
        if self.moved == False:
            for i in [(self.square[0] + i[0], self.square[1] + i[1]) for i in self.move_set]:
                if b.board[i] == '..':
                    self.possible_moves[i] = 'Empty'
                else:
                    break
        else:
            if b.board[(self.square[0] + 1, self.square[1])] == '..':
                self.possible_moves[(self.square[0] + 1, self.square[1])] = 'Empty'
        # Enemy Spaces
        for i in [(self.square[0] + i[0], self.square[1] + i[1]) for i in self.move_set_enemy]:
            if i in b.board.keys() and b.board[i] != '..' and b.board[i].isupper() != self.name.isupper():
                self.possible_moves[i] = 'Enemy'
        return self.possible_moves

class Knight(Piece):

    def __init__(self, b, team, square, name):
        self.team = team
        self.square = square
        self.name = name
        self.moved = False
        self.move_set = [(2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]
        self.possible_moves = self.move_search(b)
        b.board[square] = self.name

    def move_search(self, b):
        self.possible_moves = {}
        for i in [(self.square[0] + i[0], self.square[1] + i[1]) for i in self.move_set]:
            if i in b.board.keys() and b.board[i] == '..':
                self.possible_moves[i] = 'Empty'
        for i in [(self.square[0] + i[0], self.square[1] + i[1]) for i in self.move_set]:
            if i in b.board.keys() and b.board[i] != '..' and b.board[i].isupper() != self.name.isupper():
                self.possible_moves[i] = 'Enemy'
        return self.possible_moves

        print(self.possible_moves)
        return self.possible_moves

class Bishop(Piece):
    def __init__(self, b, team, square, name):
        self.team = team
        self.square = square
        self.name = name
        self.moved = False
        self.move_set = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8),
                         (-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6), (-7, 7), (-8, 8),
                         (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7), (8, -8),
                         (-1, -1), (-2, -2), (-3, -3), (-4, -4), (-5, -5), (-6, -6), (-7, -7), (-8, -8)]
        self.possible_moves = self.move_search(b)
        b.board[square] = self.name

    def move_search(self, b):
        self.possible_moves = {}
        for i in [(self.square[0] + i[0], self.square[1] + i[1]) for i in self.move_set]:
            if i in b.board.keys() and b.board[i] == '..':
                self.possible_moves[i] = 'Empty'
            else:
                break
        for i in [(self.square[0] + i[0], self.square[1] + i[1]) for i in self.move_set]:
            if i in b.board.keys() and b.board[i] != '..' and b.board[i].isupper() != self.name.isupper():
                self.possible_moves[i] = 'Enemy'
            else:
                break
        return self.possible_moves

        print(self.possible_moves)
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
        self.P1 = Pawn(b=self.board, team='White', square=(1, 1), name='P1')
        self.P2 = Pawn(b=self.board, team='White', square=(1, 2), name='P2')
        self.P3 = Pawn(b=self.board, team='White', square=(1, 3), name='P3')
        self.K0 = Knight(b=self.board, team='White', square=(0,1), name='K0')
        self.B0 = Bishop(b=self.board, team='White', square=(0,2), name='B0')


    def move(self, b, p, dest):
        if p.possible_moves.get(dest, 'Invalid') == 'Empty':
            b.board[p.square] = '..'
            b.board[dest] = p.name
            p.square = dest
            p.moved = True
        elif p.possible_moves.get(dest, 'Invalid') == 'Enemy':
            if b.board[dest].isupper:
                self.board.white_graveyard.append(b.board[dest])
            else:
                self.board.black_graveyard.append(b.board[dest])
            b.board[p.square] = '..'
            b.board[dest] = p.name
            p.square = dest
            print('Piece Taken!')
            p.moved = True
        elif p.possible_moves.get(dest, 'Invalid') == 'Invalid':
            print('Invalid Move! Valid moves are:')
            for i in p.possible_moves.keys():
                print(i, end = ', ')

    #def mate_check

    def play(self, b):
        print('Game Starting!')
        while self.game == True:
            self.team_turn = next(self.teams)
            while self.turn == True:
                g.board.print_board()
                print('Turn: '+self.team_turn)
                while True:
                    piece_input = input('Choose a piece: ')
                    eval('g.' + piece_input).move_search(g.board)
                    print(eval('g.'+piece_input).possible_moves.keys())
                    dest_input = str(input('Choose a destination square: '))
                    print(eval('g.'+piece_input))
                    print( eval('g.'+piece_input).possible_moves.keys() )
                    if eval(dest_input) not in eval('g.'+piece_input).possible_moves.keys():
                        print('Invalid square.  Please try again.')
                    else:
                        g.move(b=g.board, p=eval('g.'+piece_input), dest=eval(dest_input))
                        break
                print('new square: ', eval('g.'+piece_input).square)
                print('move over!')
                break







g = Game()
g.play(g.board)





