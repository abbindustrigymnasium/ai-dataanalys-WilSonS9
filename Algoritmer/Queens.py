n = 12

def createBoard(r, c):
    r, c = r-1, c-1
    board = {}
    availables = []
    for x in range(c+1):
        for y in range(r+1):
            board[(x, y)] = {'coords': (
                x, y), 'queen': False}
            availables.append((x, y))
    return (board, availables)

(board, availables) = createBoard(n, n)

def placeQueen(pos, availables, board):
    board2 = board
    board2[pos]['queen'] = True
    left = []
    x = pos[0]
    y = pos[1]
    for coord in availables:
        avail = True
        if coord[0] == x or coord[1] == y:
            avail = False
        elif abs((y - coord[1]) / (x - coord[0])) == 1:
            avail = False
        if avail:
            left.append(coord)
    removeds = set(availables) - set(left)
    return (left, board2, removeds)

def removeQueen(pos, availables, board, removeds):
    board2 = board
    board2[pos]['queen'] = False
    left = availables
    for coord in removeds:
        left.append(coord)
    return (left, board2)

(left, board2, rem) = placeQueen((0, 0), availables, board)
(left, board2) = removeQueen((0, 0), availables, board, rem)

def printBoard(n, board, left):
    for r in range(n):
        s = ''
        for c in range(n):
            if board2[c, r]['queen']:
                s += 'Q '
            elif (r, c) in left:
                s += 'O '
            else:
                s += 'X '
        print(s)
    print()

def solve(row, n, availables, board):
    if row == n:
        return (board, True, availables)
    else:
        for col in range(n):
            if (col, row) in availables:
                (availables, board, rem) = placeQueen((col, row), availables, board)
                if solve(row+1, n, availables, board)[1]:
                    return (board, True, availables)
                else:
                    (availables, board) = removeQueen((col, row), availables, board, rem)
    return (board, False, availables)

(board, solvable, left) = solve(0, n, left, board2)

printBoard(n, board, left)