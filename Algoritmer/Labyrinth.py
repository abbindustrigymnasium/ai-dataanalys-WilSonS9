from queue import LifoQueue
from numpy import inf


def createBoard(r, c):
    r, c = r-1, c-1
    board = {}
    for x in range(c+1):
        for y in range(r+1):
            wall = x == c or y == r or x == 0 or y == 0
            wall = True
            neighbours = []
            cost = 1
            for x2 in range(-1, 2):
                for y2 in range(-1, 2):
                    if x + x2 in range(c+1) and y + y2 in range(r+1):
                        if not (x + x2, y + y2) == (x, y):
                            if x2**2 + y2**2 <= 1:
                                isWall = x + x2 == c or y + y2 == r or x + x2 == 0 or y + y2 == 0
                                neighbours.append((x + x2, y + y2))
            board[(x, y)] = {'wall': wall, 'coords': (
                x, y), 'neighbours': neighbours, 'cost': cost}
    return board

board = createBoard(10, 10)

board[(1, 0)]['wall'] = False
board[(1, 1)]['wall'] = False
board[(1, 2)]['wall'] = False
board[(1, 3)]['wall'] = False
board[(1, 4)]['wall'] = False
board[(2, 4)]['wall'] = False
board[(3, 4)]['wall'] = False
board[(4, 4)]['wall'] = False
board[(5, 4)]['wall'] = False
board[(5, 3)]['wall'] = False
board[(5, 2)]['wall'] = False
board[(5, 1)]['wall'] = False
board[(6, 1)]['wall'] = False
board[(7, 1)]['wall'] = False
board[(8, 1)]['wall'] = False
board[(8, 2)]['wall'] = False
board[(8, 3)]['wall'] = False
board[(8, 4)]['wall'] = False
board[(3, 5)]['wall'] = False
board[(3, 6)]['wall'] = False
board[(3, 7)]['wall'] = False
board[(4, 7)]['wall'] = False
board[(5, 7)]['wall'] = False
board[(6, 7)]['wall'] = False
board[(7, 7)]['wall'] = False
board[(8, 7)]['wall'] = False
board[(8, 8)]['wall'] = False
board[(8, 6)]['wall'] = False
board[(8, 5)]['wall'] = False
board[(8, 9)]['wall'] = False


print(board[(1, 1)])

start = (1, 0)
goal = (8, 9)

def aStarSearch(start, goal):
    localRoot = board[start]
    stack = LifoQueue()
    bestCost = inf
    bestPath = []
    paths = []
    stack.put((localRoot, [], 0))
    while not stack.empty():
        currentNode, currentPath, currentCost = stack.get()
        paths.append((currentNode['coords'], currentCost))
        if currentNode['coords'] == goal:
            if currentCost < bestCost:
                bestCost = currentCost
                bestPath = currentPath
        else:
            children = currentNode['neighbours']
            for child in children:
                if board[child]['wall'] == False:
                    child = board[child]
                    aExplored = False
                    for path in paths:
                        if path[0] == child['coords'] and path[1] <= currentCost + child['cost']:
                            aExplored = True
                    if not aExplored:
                        stack.put(
                            (child, currentPath + [child['coords']], currentCost + child['cost']))
                        paths.append((currentNode['coords'], currentCost))
    return (bestCost, bestPath)

path = aStarSearch(start, goal)[1]
print(path)

for r in range(10):
    s = ''
    for c in range(10):
        if board[(r, c)]['wall'] == True:
            s += 'X '
        elif (r, c) == start:
            s += 's '
        elif (r, c) == goal:
            s += 'g '
        elif (r, c) in path:
            s += 'o '
        else:
            s += '* '
    print(s)
