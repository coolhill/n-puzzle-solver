from copy import deepcopy
from random import random


class Node:
    def __init__(self, q=None, size=None, h=None, g=None, f=None, parent=None):
        self.q = q     # positions
        self.h = h     # heuristic
        self.g = g     # moves
        self.f = f
        self.size = size 
        self.parent = parent

    # swap with zero
    def swap(self, x, y, goal): 

        for a in self.q:
            if 0 in a:
                self.q[self.q.index(a)][a.index(0)] = self.q[x][y]
                    
        self.q[x][y] = 0
        self.h = heuristic(self.q, goal, self.size) # heuristic has to be reevaluated


# Solve using A* algoritm
def a_star(start, goal, size):

    openNodes = [start]
    closedNodes = []

    start.h = heuristic(start.q, goal, size)
    start.g = 0 # cost from start to start is zero
    start.f = heuristic(start.q, goal, size) # in beginning f is completely heuristic

    while openNodes:

        current = sorted(openNodes, key=lambda x: x.f)[0]

        if current.q == goal:
            path = []
            while current.parent:
                path.append(current.parent)
                current = current.parent
            return path

        openNodes.remove(current)
        closedNodes.append(current)

        for node in childrenOf(current, goal):

            if node.q == goal:
                path = []
                while current.parent:
                    path.append(current.parent)
                    current = current.parent
                return path

            if node in closedNodes:
                continue

            if node in openNodes:
                new_g = current.g + 1
                if node.g > new_g:
                    node.g = new_g
                    node.parent = current
                
            else:
                node.g = current.g + 1
                node.h = heuristic(node.q, goal, size)
                node.f = node.g + node.h
                node.parent = current
                openNodes.append(node)

# Generate successor-nodes of parent
def childrenOf(parent, goal):
            
    children = []

    for i in moves(parent.q, parent.size):

        node = deepcopy(parent)
        
        for a in node.q:
            if i in a:
                x = node.q.index(a)
                y = a.index(i)

        node.swap(x, y, goal)
        
        children.append(node)

    return children


# Return array of legal moves.
def moves(m, size):

    moves = []
    for i in m:
        if (0 in i and m.index(i) != 0): # left?
            moves.append(m[m.index(i) - 1][i.index(0)])

        if (0 in i and m.index(i) != size - 1): # right?
            moves.append(m[m.index(i) + 1][i.index(0)])
        
        if (0 in i and i.index(0) != 0): # up?
            moves.append(m[m.index(i)][i.index(0) - 1])

        if (0 in i and i.index(0) != size - 1): # down?
            moves.append(m[m.index(i)][i.index(0) + 1])

    return moves

# Return shuffled array
def shuffle(q, size, howmanytimesdoyouwanttoshuffle):

    node = deepcopy(Node(q, size))

    while(howmanytimesdoyouwanttoshuffle != 0):
        move = moves(node.q, size)[round(random()*len(moves(node.q, size))) - 1]
        
        for a in node.q:
            if move in a:
                x = node.q.index(a)
                y = a.index(move)

        node.swap(x, y, q)

        howmanytimesdoyouwanttoshuffle = howmanytimesdoyouwanttoshuffle - 1

    return node

# Manhattan distance heuristic
def heuristic(n, goal, size):

    distance = 0
    for i in range(0, size - 1):
        for j in range(0, size - 1):
            if n[i][j] == goal[i][j]: break # break if no displacement

            for a in goal:
                if n[i][j] in a:
                    x = goal.index(a)
                    y = a.index(n[i][j])
                
            distance += abs(i - x) + abs(j - y) # sum of deltas in axis

    return distance

def solve():

    goal = [[1,   2,  3,  4],
            [5,   6,  7,  8],
            [9,  10, 11, 12],
            [13, 14, 15,  0]]

    start = shuffle(goal, 4, 10).q
    
    for a in a_star(Node(start, 4), goal, 4):
        for b in a.q:
            print(b)
        print("")

if __name__ == '__main__':
    solve()
