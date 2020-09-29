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
            return False
        # checking square avalaibility and placing the piece
        if self._board[crds[sq][0]][crds[sq][1]] == '-':
            self._board[crds[sq][0]][crds[sq][1]] = pc
        else:
            print("error: square is taken!")
            return False
        return True
