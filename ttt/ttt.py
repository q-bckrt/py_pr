from termcolor import colored, cprint

class Board:
    # initializing the board in the form of a 2-dimensional list
    def __init__(self):
        self._board = [['-' for i in range(0, 3)] for i in range(0,3)]
    
    # display the board in its current state
    def display(self):
        print("")
        for row in self._board:
            print(f"  {row[0]}|{row[1]}|{row[2]}")
        print("")

    # place x's and o's onto the board
    def play(self, sq, pc):
        # turning the square number into usable board coordinates
        crds = {
            1: [0, 0],
            2: [0, 1],
            3: [0, 2],
            4: [1, 0],
            5: [1, 1],
            6: [1, 2],
            7: [2, 0],
            8: [2, 1],
            9: [2, 2]
                }
        # checking square avalaibility and placing the piece
        if self._board[crds[sq][0]][crds[sq][1]] == '-':
            self._board[crds[sq][0]][crds[sq][1]] = pc
        else:
            print("error: square is taken!")
            return -2
        return 1

    def is_win(self):
        if (self._board[0][0] == self._board[1][1] == self._board[2][2]
        and self._board[0][0] != '-'):
            return (0, "\\")
        if (self._board[0][2] == self._board[1][1] == self._board[2][0]
        and self._board[0][2] != '-'):
            return (0, "/")
        for i in range(0, 3):
            if (self._board[i][0] == self._board[i][1] == self._board[i][2]
            and self._board[i][0] != '-'):
                return (i, "_")
            if (self._board[0][i] == self._board[1][i] == self._board[2][i]
            and self._board[0][i] != '-'):
                return (i, "|")
        return (False)


def get_player_move(pn, player):
    pieces = '-'
    if pn == 1:
        pieces = colored('x', color="cyan")
    else:
        pieces = colored('o', color="magenta")
    try:
        ret = int(input(f"player {player} > choose square number:"))
    except ValueError:
        print("please enter a number between 1 and 9.")
        return 0, pieces
    else:
        if ret < 1 or ret > 9:
            print("please enter a number between 1 and 9.")
            return 0, pieces
        return ret, pieces

def get_player_color(pn):
    if pn == 1:
        return colored(str(pn), color="magenta")
    else:
        return colored(str(pn), color="cyan")

def color_winning_line(board, idx, direction, pn):
    pieces = ""
    if pn == 1:
        pieces = 'x'
    else:
        pieces = 'o'
    if direction == "/":
        board._board[0][2] = colored(pieces, "green")
        board._board[1][1] = colored(pieces, "green")
        board._board[2][0] = colored(pieces, "green")
    elif direction == "\\":
        for i in range(0,3):
            board._board[i][i] = colored(pieces, "green")
    elif direction == "_":
        for i in range(0, 3):
            board._board[idx][i] = colored(pieces, "green")
    elif direction == "|":
        for i in range(0, 3):
            board._board[i][idx] = colored(pieces, "green")
    return board

# initialize
cprint("~tic-tac-toe~", color="yellow")
board = Board()
board.display()
turn = 0

# main game loop
while True:
    pn = (turn % 2) + 1
    player = get_player_color(pn)
    ret = 0
    while ret <= 0:
        place, pieces = get_player_move(pn, player)
        if place == 0:
            continue
        ret = board.play(place, pieces)
    w = board.is_win()
    if w:
        print(f"Player {player} wins!")
        color_winning_line(board, w[0], w[1], pn).display()
        break
    board.display()
    if turn == 8:
        break
    turn += 1
