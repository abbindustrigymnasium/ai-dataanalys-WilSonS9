from queue import LifoQueue
from numpy import inf


class node:
    def __init__(self, val, cost):
        self.val = val
        self.l = None
        self.r = None
        self.cost = cost


root = node('A', 0)
root.l = node('B', 9)
root.l.r = node('E', 5)
root.r = node('C', 10)
root.r.l = node('D', 4)
root.r.r = node('E', 7)
root.r.r.l = node('F', 5)
root.r.l.l = node('F', 3)
root.l.r.l = node('F', 3)


def dfs(node, visited, goal):
    if not node is None:
        if not node.val in visited:
            if node.val == goal:
                return node
            else:
                print(node.val)
                visited.append(node.val)
                g = dfs(node.l, visited, goal)
                if g is None:
                    g = dfs(node.r, visited, goal)
                return g


# visited = dfs(root, [], 'F')


def bfs(node, visited):
    if not node is None:
        if not node.val in visited:
            print(node.val)
            visited.append(node.val)
        if not node.l is None and not node.l.val in visited:
            print(node.l.val)
            visited.append(node.l.val)
        if not node.r is None and not node.r.val in visited:
            print(node.r.val)
            visited.append(node.r.val)
        bfs(node.l, visited)
        bfs(node.r, visited)
    return visited


# visited = bfs(root, [])

def ucs(start, goal):
    localRoot = dfs(root, [], start)
    stack = LifoQueue()
    bestCost = inf
    bestPath = []
    visited = []
    stack.put((localRoot, [], 0))
    while not stack.empty():
        currentNode, currentPath, currentCost = stack.get()
        if not currentNode.val in visited or currentCost < bestCost:
            visited.append(currentNode.val)
            if currentNode.val == goal and currentCost < bestCost:
                bestCost = currentCost
                bestPath = currentPath
            else:
                children = [currentNode.l, currentNode.r]
                for child in children:
                    if not child is None:
                        stack.put(
                            (child, currentPath + [child.val], currentCost + child.cost))
    return (bestCost, bestPath)


# print(ucs('A', 'F'))

def greedyBestFirst(start, goal):
    localRoot = dfs(root, [], start)
    stack = LifoQueue()
    bestCost = 1000000
    bestPath = []
    visited = []
    stack.put((localRoot, [], 0))
    while not stack.empty():
        currentNode, currentPath, currentCost = stack.get()
        if not currentNode.val in visited or currentCost < bestCost:
            visited.append(currentNode.val)
            if currentNode.val == goal and currentCost < bestCost:
                bestCost = currentCost
                bestPath = currentPath
            else:
                children = [currentNode.l, currentNode.r]
                best = 10000
                choice = None
                for child in children:
                    if not child is None:
                        if child.cost < best:
                            best = child.cost
                            choice = child
                stack.put(
                    (choice, currentPath + [choice.val], currentCost + best))
    return (bestCost, bestPath)


# print(greedyBestFirst('A', 'E'))

def aStarSearch(start, goal):
    localRoot = dfs(root, [], start)
    stack = LifoQueue()
    bestCost = 1000000
    bestPath = []
    paths = []
    stack.put((localRoot, [], 0))
    while not stack.empty():
        currentNode, currentPath, currentCost = stack.get()
        paths.append((currentNode.val, currentCost))
        if currentNode.val == goal:
            return (currentCost, currentPath)
        else:
            children = [currentNode.l, currentNode.r]
            for child in children:
                aExplored = False
                if not child is None:
                    for path in paths:
                        if path[0] == child.val and path[1] <= currentCost + child.cost:
                            print('irtughe')
                            aExplored = True
                    if not aExplored:
                        stack.put(
                            (child, currentPath + [child.val], currentCost + child.cost))
                        paths.append((currentNode.val, currentCost))
    return (bestCost, bestPath)


print(aStarSearch('A', 'F'))
