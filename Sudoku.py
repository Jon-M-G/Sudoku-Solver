# define the board
board = [
    [0,8,0,0,0,0,0,3,2],
    [4,0,0,0,0,6,5,0,0],
    [0,0,0,0,3,0,1,0,0],
    [0,0,3,6,0,5,4,0,0],
    [1,0,0,0,0,0,0,0,6],
    [0,0,4,8,0,7,9,0,0],
    [0,0,9,0,5,0,0,0,0],
    [0,0,8,7,0,0,0,0,9],
    [6,2,0,0,0,0,0,8,0]
    ]


def canPlace(num, row, column):
    # check that the n is not also somewhere in that row
    for i in range(len(board)):
        if board[i][column] == num:
            return False

    for i in range(len(board)):
        if board[row][i] == num:
            return False

    # Sudoku sub board start positions for row and columns
    subTableRowStart = (row//3)*3
    subTableColumnStart = (column//3)*3

    # checking if that sub board has that same number in it
    for i in range(subTableRowStart,subTableRowStart+3):
        for j in range(subTableColumnStart,subTableColumnStart+3):
            if board[i][j] == num:
                return False
    return True


def SolveCheck(row, column):
    default = 0
    for i in range(0, len(board)):
        for j in range (0, len(board)):
            # check if there is a value in that
            if board[i][j] == 0:
                row = i
                column = j
                default = 1
                subBoard = [row, column, default]
                return subBoard
    # use -1 to indicate that the puzzle has been solved
    subBoard = [-1, -1, default]
    return subBoard


def solve():
    rowNum = columnNum = 0
    # If all subBoards are filled then we're done
    subBoard = SolveCheck(rowNum, columnNum)
    if subBoard[2] == 0:
        return True
    rowNum = subBoard[0] # Get row number
    columnNum = subBoard[1]  # get column number

    for i in range(1,10):
        if canPlace(i, rowNum, columnNum):
            board[rowNum][columnNum] = i
            # if it doesnt work backtrack
            if solve():
                return True
            # If this solution doesnt work then reset the value
            board[rowNum][columnNum] = 0
    return False

# print the sudoku board
def printBoard():
    for slot in board:
        print(slot)


# solve the puzzle and print it
solve()
printBoard()
