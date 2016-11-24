from copy import deepcopy

class Node:
    def __init__(self, q=None, h=None, g=None, f=None, parent=None):
        self.q = q     # positions
        self.h = h     # heuristic
        self.g = g     # moves
        self.f = f 
        self.parent = parent

    # swap with zero
    def swap(self, xPos, yPos): 

        for a in self.q:
            if 0 in a:
                self.q[self.q.index(a)][a.index(0)] = self.q[xPos][yPos]
                    
        self.q[xPos][yPos] = 0
        self.h = heuristic(self.q, goal) # heuristic has to be reevaluated

# Solve using A* algoritm
def solve(start, goal):

    openNodes = [start]
    closedNodes = []

    start.h = heuristic(start.q, goal)
    start.g = 0 # cost from start to start is zero
    start.f = heuristic(start.q, goal) # in beginning f is completely heuristic

    while openNodes:

        current = lowest_fCost(openNodes)

        if current.q == goal:
            path = []
            recalc_path(current)
            return path

        openNodes.remove(current)
        closedNodes.append(current)

        for node in childrenOf(current):

            flag = False
            if node.q == goal:
                path = []
                recalc_path(current, path)
                return path
            
            for a in openNodes:
                if a.q == node.q and a.f <= node.f: flag = True
            for a in closedNodes:
                if a.q == node.q and a.f <= node.f: flag = True
            if flag: continue

            openNodes.append(node)


def recalc_path(node, path):
    path.append(node)
    if node.parent != None: 
        recalc_path(node.parent, path)


def lowest_fCost(nodes):
    return sorted(nodes, key=lambda x: x.f, reverse=True)[-1]


# Generate successor-nodes of parent
def childrenOf(parent):
            
    children = []

    for i in moves(parent.q):

        node = deepcopy(parent)
        
        for a in node.q:
            if i in a:
                xPos = node.q.index(a)
                yPos = a.index(i)

        node.swap(xPos, yPos)
        node.parent = parent
        node.h = heuristic(node.q, goal)
        node.g = node.g + 1
        node.f = node.g + node.h
        
        children.append(node)

    return children


# Return array of legal moves.
def moves(m):

    moves = []
    for i in m:
        if (0 in i and m.index(i) != 0): # left?
            moves.append(m[m.index(i) - 1][i.index(0)])

        if (0 in i and m.index(i) != 3): # right?
            moves.append(m[m.index(i) + 1][i.index(0)])
        
        if (0 in i and i.index(0) != 0): # up?
            moves.append(m[m.index(i)][i.index(0) - 1])

        if (0 in i and i.index(0) != 3): # down?
            moves.append(m[m.index(i)][i.index(0) + 1])

    return moves
    
# Manhattan distance heuristic    
def heuristic(n, goal):

    distance = 0
    for i in range(0,3):
        for j in range(0,3):
            if n[i][j] == goal[i][j]: break # break if no displacement

            for a in goal:
                if n[i][j] in a:
                    x = goal.index(a)
                    y = a.index(n[i][j])
                
            distance += abs(i - x) + abs(j - y) # sum of deltas in axis

    return distance

if __name__ == '__main__':
    goal = [[1,   2,  3,  4],
            [5,   6,  7,  8],
            [9,  10, 11, 12],
            [13, 14, 15,  0]]

    start = Node([[2,   3,  4,  8],
                  [1,   5,  6,  0],
                  [10,  11, 7, 12],
                  [9, 13, 14,  15]])
    
    for a in solve(start, goal):
        for b in a.q:
            print(b)
        print("")
