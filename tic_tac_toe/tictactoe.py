import numpy as np


class TicTacToe():
    def __init__(self):
        player1 = Player(input('Player 1, What is your name?'), 'x')
        player2 = Player(input('Player 2, What is your name?'), 'o')
        self.players = [player1, player2]

        for p in self.players:
            print(f"Welcome to the game, {p.name}! You are playing {p.marker}'s")

        self.game_board = Board()

        instructions = '''
        Welcome to Tic Tac Toe (It's fun playing a game...of tic...tac toe).
        
        Press q to quit.
        
        '''
        print(instructions)

    def play(self):

        running = True
        round = 1

        while running:
            current_player = self.players[round % 2]

            print(f"Player: {current_player.name}")

            self.game_board.display_board()

            chosen_row = int(input("Pick a Row (q to quit) >>> "))
            chosen_column = int(input("Pick a Column (q to quit) >>> "))

            if chosen_column == 'q' or chosen_row == 'q':
                break

            print(f"{current_player.name} has chosen to place a marker at {chosen_row, chosen_column}")

            self.game_board.place_marker(current_player.draw_marker(), chosen_row, chosen_column)

            print("Check winning conditions and decide to end game.")

            round += 1



class Marker():
    def __init__(self, icon):
        self.icon = icon

    def underline_icon(self):
        return self.icon + '\n__'


class Board():
    def __init__(self):
        self.board = self.draw_board()


    def draw_board(self):
        '''Generates a NEW board (consider changing the function name...'''

        board = []

        for r in range(3):
            board.append([])

        for r in range(3):
            for c in range(3):
                board[r].append('')
        print(board)
        return board

    def display_board(self):
        '''Prints the board as it exists in the current state.'''

        for row in self.board:
            print('\t'.join([x.replace('','_') for x in row]))



    def place_marker(self, marker_object, row, column):

        #   Correct for "human" row and column numbers... (avoid 'off by one' errors).
        row -= 1
        column -= 1

        self.board[row][column] = marker_object.icon
        return self.board

    def check_rows(self, board=None):

        #   Since self is checked at function call time, it's impossible to use it when defining a variable.
        if board == None:
            board = self.board

        rownum = 1
        for row in board:
            if len(set(row)) == 1 and set(row) != {''}:
                return set(row).pop()
            else:
                rownum += 1
        return False

    def check_columns(self):
        numpy_array = np.array(self.board)
        transpose = numpy_array.T
        transpose_list = transpose.tolist()
        print('Checking Columns:')
        return self.check_rows(transpose_list)

    def check_diagonals(self, board = None):

        if board == None:
            board = self.board

        diagonals = [[],[]]
        for i in range(len(board)):
            diagonals[0].append(self.board[i][i])

        row = 1
        for i in reversed(range(len(board))):
            diagonals[1].append(self.board[row][i])
            row == 1

        print('checking diagonals, which means checking rows...')
        return self.check_rows(diagonals)


    def check_winning_conditions(self):
        (rows, columns, diagonals) = self.check_rows(), self.check_columns(), self.check_diagonals()

        winning_conditions = {rows, columns, diagonals}
        if len(winning_conditions) > 1:
            print('checking winning conditions', winning_conditions)
            return winning_conditions.difference({False}).pop()
        else:
            return False


class Player():
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

    def draw_marker(self):
        return Marker(self.marker)



game_board = Board()

jonathan = Player('Jonathan','x')
samantha = Player('Samantha','o')


[print(x) for x in game_board.place_marker(samantha.draw_marker(), 1, 1)]
print()
[print(x) for x in game_board.place_marker(samantha.draw_marker(), 1, 2)]
print()
[print(x) for x in game_board.place_marker(samantha.draw_marker(), 3, 3)]
print()
[print(x) for x in game_board.place_marker(samantha.draw_marker(), 2, 2)]
print()

print(game_board.check_winning_conditions())

game = TicTacToe()
game.play()
