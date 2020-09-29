from termcolor import colored

class Board:
    # initializing the board in the form of a 2-dimensional list
    def __init__(self):
        self._board = [['-' for i in range(0, 3)] for i in range(0,3)]
    
    # display the board in its current state
    def display(self):
        for row in self._board:
            print(f"{row[0]}|{row[1]}|{row[2]}")
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
        # checking arguments validity
        try:
            if type(sq) != int or type(pc) != str:
                raise TypeError
            if sq < 1 or sq > 9:
                raise ValueError
            if pc != 'x' and pc != 'o':
                raise ValueError
        except:
            print("error: Board.play() has been passed wrong arguments")
            return -1
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
            return True
        if (self._board[0][2] == self._board[1][1] == self._board[2][0]
        and self._board[0][2] != '-'):
            return True
        for i in range(0, 3):
            if (self._board[i][0] == self._board[i][1] == self._board[i][2]
            and self._board[i][0] != '-'):
                return True
            if (self._board[0][i] == self._board[1][i] == self._board[2][i]
            and self._board[i][0] != '-'):
                return True
        return False
            

def get_player_move(player):
    pieces = '-'
    if player == '1':
        pieces = 'x'
    else:
        pieces = 'o'
    return int(input(f"player {player} > choose square number: ")), pieces

def get_player_color(turn):
    pn = (turn % 2) + 1
    if pn == 1:
        return colored(str(pn), color="magenta")
    else:
        return colored(str(pn), color="cyan")

# initialize
board = Board()
board.display()
turn = 0

# main game loop
while True:
    player = get_player_color(turn)
    ret = 0
    while ret <= 0:
        place, pieces = get_player_move(player)
        ret = board.play(place, pieces)

    board.display()
    if board.is_win():
        print(f"Player {player} wins!")
        break
    if turn == 8:
        break
    turn += 1

