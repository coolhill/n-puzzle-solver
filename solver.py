from copy import deepcopy

class Node:
    def __init__(self, board=None, heuristic=None, gScore=None, fScore=None, parent=None):
        self.board = board
        self.heuristic = heuristic
        self.gScore = gScore
        self.fScore = fScore
        self.parent = parent

    # swap with zero
    def swap(self, xPos, yPos): 

        for a in self.board:
            if 0 in a:
                self.board[self.board.index(a)][a.index(0)] = self.board[xPos][yPos]
                    
        self.board[xPos][yPos] = 0
        self.heuristic = heuristic(self.board, goal) # heuristic has to be reevaluated

# Solve using A* algoritm
def solve(start, goal):

    openNodes = [start]
    closedNodes = [] 

    start.heuristic = heuristic(start.board, goal)
    start.gScore = 0 # cost from start to start is zero
    start.fScore = heuristic(start.board, goal) # in beginning fScore is completely heuristic

    while openNodes:

        current = lowest_fCost(openNodes)

        if current.board == goal: break

        openNodes.remove(current)
        closedNodes.append(current)

        for node in childrenOf(current):

            for a in openNodes:
                if a.board == node.board and a.fScore <= node.fScore: continue # This is not a better path!

            for a in closedNodes:
                if a.board == node.board and a.fScore <= node.fScore: continue 

            openNodes.append(node)


def lowest_fCost(nodes):

    return sorted(nodes, key=lambda x: x.fScore, reverse=True)[0]


# Generate successor-nodes of parent
def childrenOf(parent):
            
    children = []

    for i in moves(parent.board):

        node = deepcopy(parent)
        
        for a in node.board:
            if i in a:
                xPos = node.board.index(a)
                yPos = a.index(i)

        node.swap(xPos, yPos)
        node.parent = parent
        node.gScore = node.gScore + 1
        node.fScore = node.gScore + node.heuristic
        
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
                for b in a:
                    if b == n[i][j]:
                        x = goal.index(a)
                        y = a.index(b)
                
            distance += abs(i - x) + abs(j - y) # sum of deltas in axis

    return distance

if __name__ == '__main__':
    goal = [[1,   2,  3,  4],
            [5,   6,  7,  8],
            [9,  10, 11, 12],
            [13, 14, 15,  0]]

    start = Node([[1,   2,  3,  4],
                  [5,   6,  7,  8],
                  [9,  10, 11, 12],
                  [13, 14, 0,  15]])


    
    solve(start, goal)
