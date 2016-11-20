from copy import deepcopy

# Experimental first generation of linked list solution. Linked lists
# are made up of nodes, where each node contains a reference to the
# next node in the list. In addition, each node contains a unit of
# data called the cargo(board).

class Node:
    def __init__(self, board=None, parent=None):
        self.board = board
        # self.heuristic = heuristic     # h-value
        # self.moves = moves             # g-value
        self.parent = parent

    def swap(self, xPos, yPos): # swap with zero

        for a in self.board:
            if 0 in a:
                self.board[self.board.index(a)][a.index(0)] = self.board[xPos][yPos]
                    
        self.board[xPos][yPos] = 0

goal = [[1,   2,  3,  4],
        [5,   6,  7,  8],
        [9,  10, 11, 12],
        [13, 14, 15,  0]]

start = Node([[1,   2,  3,  4],
              [8,   5,  6,  7],
              [9,   10, 11, 0],
              [12, 13, 14, 15]])

openNodes = [start]
closedNodes = []


# Solve using A* algoritm
def solve(current, goal):

    gen_nodes(moves(current.board), current)

    for a in openNodes:
        print(a.board)

    
def gen_nodes(n, current):
            
    # Generate successor-nodes (by the 0's grannar)
    for i in n:

        new = deepcopy(current)
        
        # replace 0 with i and i with 0
        for a in new.board:
            if i in a:
                xPos = new.board.index(a)
                yPos = a.index(i)

        new.swap(xPos, yPos)

        if closedNodes.count(new) == 1: break
        openNodes.append(new)

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
def heuristic(n):

    distance = 0
    for i in range(0,3):
        for j in range(0,3):
            if n[i][j] == goal[i][j]: break # if no displacement -> break

            for a in goal:
                for b in a:
                    if b == n[i][j]:
                        x = goal.index(a)
                        y = a.index(b)
                
            distance += abs(i - x) + abs(j - y) # sum of deltas in axis

    return distance

if __name__ == '__main__':
    
    solve(start, goal)
#    print("skoj")
