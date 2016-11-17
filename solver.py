goal = [[1,   2,  3,  4],
        [5,   6,  7,  8],
        [9,  10, 11, 12],
        [13, 14, 15,  0]]

start = [[1,   2,  3,  4],
         [8,   5,  6,  7],
         [9,   10, 11, 0],
         [12, 13, 14, 15]]

openNodes = [[start]]
closedNodes = []

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

    def getBoard(self):
        return self.board

    def switch(xPos, yPos): # switch with zero

        for a in self.board:
            for b in a:
                if b == 0:
                    self.board[self.board.index(a)][a.index(b)] = self.board[xPos][yPos]
                    
        self.board[xPos][yPos] = 0

        
# Solve using A* algoritm
def solve(current, goal):

    gen_nodes(moves(current), current)
    
    # if closedNodes.count(new) == 1: break
    # openNodes.append(new.insert(current.index(0), granne))
        
    
def gen_nodes(m, cur):
            
    # Generate successor-nodes (by the 0's grannar)
    for i in m:
        print(i)

        new = Node(cur) # maybe this will fix concurrency bug

        # There is a problem with commented code below. Uncomment and
        # see compilor error.
        
        # replace 0 with i and i with 0
        # for a in new.getBoard():
        #     for b in a:
        #         if b == i:
        #             print(new.getBoard().index(a))
        #             print(b)
        #             new.switch(new.getBoard().index(a), b)

        print(new.getBoard())
    
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
