end = [[1,   2,  3,  4],
       [5,   6,  7,  8],
       [9,  10, 11, 12],
       [13, 14, 15,  0]]

start = [[1,   2,  3,  4],
         [8,   5,  6,  7],
         [9,   10, 0, 11],
         [12, 13, 14, 15]]

openNodes = [[start]]
closedNodes = []

# Solve using A* algoritm
def solve(current, end):

    # Generate successor-nodes (by the 0's grannar)
    for i in moves(current):
        print(i)

        # wild west below
        new = current
        dummy = new[granne]
        new.remove(dummy)
        new.insert(current.index(0), dummy)
        new.remove(0)
        new.insert(granne, 0)
        if closedNodes.count(new) == 1:
            break
        print(current)
        print(new)
        print(heuristic(new))

        # openNodes.append(new.insert(current.index(0), granne))


# Return array of legal moves.
def moves(m):

    moves = []
    for i in m:
        if (0 in i and m.index(i) != 0):
            moves.append(m[m.index(i) - 1][i.index(0)]) # if zero is indexed in i: legal move is found.

        if (0 in i and m.index(i) != 3):
            moves.append(m[m.index(i) + 1][i.index(0)])
        
        if (0 in i and i.index(0) != 0):
            moves.append(m[m.index(i)][i.index(0) - 1])

        if (0 in i and i.index(0) != 3):
            moves.append(m[m.index(i)][i.index(0) + 1])

    return moves
    
# Manhattan distance heuristic    
def heuristic(n):

    n.insert(n.index(0), 16)
    n.remove(0)
    distance = 0
    for i in range(1, 16):
        if i == n.index(i)+1: break
        distance += abs(((i-1) - n.index(i))/4) + abs((i-1)%4 - n.index(i)%4)

    n.insert(n.index(16), 0)
    n.remove(16)
    return distance

if __name__ == '__main__':
    
    solve(start, end)
#    print("skoj")
