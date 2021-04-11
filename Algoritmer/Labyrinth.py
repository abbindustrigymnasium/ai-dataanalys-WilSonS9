from queue import LifoQueue
from numpy import inf


def createBoard(r, c):
    board = {}
    for x in range(c+1):
        for y in range(r+1):
            wall = x == c or y == r or x == 0 or y == 0
            neighbours = []
            cost = 1
            for x2 in range(-1, 2):
                for y2 in range(-1, 2):
                    if x + x2 in range(c+1) and y + y2 in range(r+1):
                        if not (x + x2, y + y2) == (x, y):
                            if x2**2 + y2**2 <= 1:
                                isWall = x + x2 == c or y + y2 == r or x + x2 == 0 or y + y2 == 0
                                if not isWall:
                                    neighbours.append((x + x2, y + y2))
            board[(x, y)] = {'wall': wall, 'coords': (
                x, y), 'neighbours': neighbours, 'cost': cost}
    return board


board = createBoard(10, 10)
board[(5, 5)]['wall'] = True
board[(5, 6)]['wall'] = True
board[(6, 6)]['wall'] = True
board[(6, 5)]['wall'] = True

print(board[(1, 1)])


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
            return (currentCost, currentPath)
        else:
            children = currentNode['neighbours']
            for child in children:
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


print(aStarSearch((1, 1), (6, 7)))
