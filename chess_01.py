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
    _registry = []

    def __init__(self, status = True):
       self.status = status
       self._registry.append(self)

    def move_search(self):
    	pass


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
        Piece.__init__(self)

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
            if b.board[(self.square[0] + self.move_set[0][0], self.square[1])] == '..':
                self.possible_moves[(self.square[0] + self.move_set[0][0], self.square[1])] = 'Empty'
        # Enemy Spaces
        for i in [(self.square[0] + i[0], self.square[1] + i[1]) for i in self.move_set_enemy]:
            if i in b.board.keys() and b.board[i] != '..' and b.board[i].isupper() != self.name.isupper():
                self.possible_moves[i] = 'Enemy'
        Piece.move_search(self)
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
        Piece.__init__(self)

    def move_search(self, b):
        self.possible_moves = {}
        for i in [(self.square[0] + i[0], self.square[1] + i[1]) for i in self.move_set]:
            if i in b.board.keys() and b.board[i] == '..':
                self.possible_moves[i] = 'Empty'
        for i in [(self.square[0] + i[0], self.square[1] + i[1]) for i in self.move_set]:
            if i in b.board.keys() and b.board[i] != '..' and b.board[i].isupper() != self.name.isupper():
                self.possible_moves[i] = 'Enemy'
        return self.possible_moves


class Bishop(Piece):
    
    def __init__(self, b, team, square, name):
        self.team = team
        self.square = square
        self.name = name
        self.moved = False
        self.move_set = [[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)],
                         [(-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6), (-7, 7), (-8, 8)],
                         [(1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7), (8, -8)],
                         [(-1, -1), (-2, -2), (-3, -3), (-4, -4), (-5, -5), (-6, -6), (-7, -7), (-8, -8)]]
        self.possible_moves = self.move_search(b)
        b.board[square] = self.name
        Piece.__init__(self)

    def move_search(self, b):
        self.possible_moves = {}
        for direction in self.move_set:
            for j in [(self.square[0] + i[0], self.square[1] + i[1]) for i in direction]:
                if j in b.board.keys() and b.board[j] == '..':
                    self.possible_moves[j] = 'Empty'
                elif j in b.board.keys() and b.board[j] != '..' and b.board[j].isupper() != self.name.isupper():
                    self.possible_moves[j] = 'Enemy'
                    break
                else:
                    break
        return self.possible_moves


class Rook(Piece):

    def __init__(self, b, team, square, name):
        self.team = team
        self.square = square
        self.name = name
        self.moved = False
        self.move_set = [[(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)],
                         [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8)],
                         [(-1, 0), (-2, 0), (-3, 0), (-4, 0), (-5, 0), (-6, 0), (-7, 0), (-8, 0)],
                         [(0, -1), (0, -2), (0, -3), (0, -4), (0, -5), (0, -6), (0, -7), (0, -8)]]
        self.possible_moves = self.move_search(b)
        b.board[square] = self.name
        Piece.__init__(self)

    def move_search(self, b):
        self.possible_moves = {}
        for direction in self.move_set:
            for j in [(self.square[0] + i[0], self.square[1] + i[1]) for i in direction]:
                if j in b.board.keys() and b.board[j] == '..':
                    self.possible_moves[j] = 'Empty'
                elif j in b.board.keys() and b.board[j] != '..' and b.board[j].isupper() != self.name.isupper():
                    self.possible_moves[j] = 'Enemy'
                    break
                else:
                    break
        return self.possible_moves



class King(Piece):

    def __init__(self, b, team, square, name):
        self.team = team
        self.square = square
        self.name = name
        self.moved = False
        self.move_set = [(1, 0), (1, 1), (0, 1), (1, -1), (-1, 0), (-1, -1), (-1, 1), (0, -1)]
        self.possible_moves = self.move_search(b)
        b.board[square] = self.name
        Piece.__init__(self)

    def move_search(self, b):
        self.possible_moves = {}
        for i in [(self.square[0] + i[0], self.square[1] + i[1]) for i in self.move_set]:
            if i in b.board.keys() and b.board[i] == '..':
                self.possible_moves[i] = 'Empty'
        for i in [(self.square[0] + i[0], self.square[1] + i[1]) for i in self.move_set]:
            if i in b.board.keys() and b.board[i] != '..' and b.board[i].isupper() != self.name.isupper():
                self.possible_moves[i] = 'Enemy'
        return self.possible_moves


class Queen(Piece):

    def __init__(self, b, team, square, name):
        self.team = team
        self.square = square
        self.name = name
        self.moved = False
        self.move_set = [[(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)],
                         [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8)],
                         [(-1, 0), (-2, 0), (-3, 0), (-4, 0), (-5, 0), (-6, 0), (-7, 0), (-8, 0)],
                         [(0, -1), (0, -2), (0, -3), (0, -4), (0, -5), (0, -6), (0, -7), (0, -8)],
                         [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)],
                         [(-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6), (-7, 7), (-8, 8)],
                         [(1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7), (8, -8)],
                         [(-1, -1), (-2, -2), (-3, -3), (-4, -4), (-5, -5), (-6, -6), (-7, -7), (-8, -8)]]
        self.possible_moves = self.move_search(b)
        b.board[square] = self.name
        Piece.__init__(self)

    def move_search(self, b):
        self.possible_moves = {}
        for direction in self.move_set:
            for j in [(self.square[0] + i[0], self.square[1] + i[1]) for i in direction]:
                if j in b.board.keys() and b.board[j] == '..':
                    self.possible_moves[j] = 'Empty'
                elif j in b.board.keys() and b.board[j] != '..' and b.board[j].isupper() != self.name.isupper():
                    self.possible_moves[j] = 'Enemy'
                    break
                else:
                    break
        return self.possible_moves


class Player:

	def __init__(self, team = 'White', CPU = False):
		self.team = team
		self.CPU = CPU
		self.wins = 0
		self.losses = 0


class Game:
    """ This class controls the flow of the game and the decision-making of the AI.  Also:
        - Function to check for game state (mate, etc.)
        - Function to check for
    """
    def __init__(self):
        self.board = Board()
        self.game = True
        self.turn = True
        self.teams = cycle(['White', 'Black'])
        self.game_type = self.game_setup()
        self.player1 = Player()
        self.player2 = self.CPU_setup()
        self.white_mate = False
        self.black_mate = False
        self.P0 = Pawn(b=self.board, team='White', square=(1, 0), name='P0')
        self.P1 = Pawn(b=self.board, team='White', square=(1, 1), name='P1')
        self.P2 = Pawn(b=self.board, team='White', square=(1, 2), name='P2')
        self.P3 = Pawn(b=self.board, team='White', square=(1, 3), name='P3')
        self.P4 = Pawn(b=self.board, team='White', square=(1, 4), name='P4')
        self.P5 = Pawn(b=self.board, team='White', square=(1, 5), name='P5')
        self.P6 = Pawn(b=self.board, team='White', square=(1, 6), name='P6')
        self.P7 = Pawn(b=self.board, team='White', square=(1, 7), name='P7')
        self.R0 = Rook(b=self.board, team='White', square=(0, 0), name='R0')
        self.R1 = Rook(b=self.board, team='White', square=(0, 7), name='R1')
        self.K0 = Knight(b=self.board, team='White', square=(0, 1), name='K0')
        self.K1 = Knight(b=self.board, team='White', square=(0, 6), name='K1')
        self.B0 = Bishop(b=self.board, team='White', square=(0, 2), name='B0')
        self.B1 = Bishop(b=self.board, team='White', square=(0, 5), name='B1')
        self.KK = King(b=self.board, team = 'White', square=(0, 3), name = 'KK')
        self.QQ = Queen(b=self.board, team = 'White', square=(0, 4), name = 'QQ')
        self.p0 = Pawn(b=self.board, team='Black', square=(6, 0), name='p0')
        self.p1 = Pawn(b=self.board, team='Black', square=(6, 1), name='p1')
        self.p2 = Pawn(b=self.board, team='Black', square=(6, 2), name='p2')
        self.p3 = Pawn(b=self.board, team='Black', square=(6, 3), name='p3')
        self.p4 = Pawn(b=self.board, team='Black', square=(6, 4), name='p4')
        self.p5 = Pawn(b=self.board, team='Black', square=(6, 5), name='p5')
        self.p6 = Pawn(b=self.board, team='Black', square=(6, 6), name='p6')
        self.p7 = Pawn(b=self.board, team='Black', square=(6, 7), name='p7')
        self.r0 = Rook(b=self.board, team='Black', square=(7, 0), name='r0')
        self.r1 = Rook(b=self.board, team='Black', square=(7, 7), name='r1')
        self.k0 = Knight(b=self.board, team='Black', square=(7, 1), name='k0')
        self.k1 = Knight(b=self.board, team='Black', square=(7, 6), name='k1')
        self.b0 = Bishop(b=self.board, team='Black', square=(7, 2), name='b0')
        self.b1 = Bishop(b=self.board, team='Black', square=(7, 5), name='b1')
        self.kk = King(b=self.board, team = 'Black', square=(7, 3), name = 'kk')
        self.qq = Queen(b=self.board, team = 'Black', square=(7, 4), name = 'qq')

    def game_setup(self):
    	self.game_type = ''
    	a = int(input('How many players are playing? '))
    	if a == 1:
    		self.game_type = 'single'
    	elif a == 2:
    		self.game_type = 'multi'
    	return self.game_type

    def CPU_setup(self):
    	if self.game_type == 'multi':
    		return Player(team = 'Black', CPU = False)
    	elif self.game_type == 'single':
    		return Player(team = 'Black', CPU = True)

    #def game_state_set(self):
    	# check is black is in mate

    #def game_state_get(self):
    	# retrieve 

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

    def play(self):
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
g.play()





