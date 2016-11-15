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

# Solve using A* algoritm
def solve(current, goal):

    # Generate successor-nodes (by the 0's grannar)
    for i in moves(current):
        print(i)

    print(heuristic(start))
        
        # wild west below
        # new = current
        # dummy = new[granne]
        # new.remove(dummy)
        # new.insert(current.index(0), dummy)
        # new.remove(0)
        # new.insert(granne, 0)
        # if closedNodes.count(new) == 1:
        #     break
        # print(current)
        # print(new)
        # print(heuristic(new))

        # openNodes.append(new.insert(current.index(0), granne))


# Return array of legal moves.
def moves(m):

    moves = []
    for i in m:
        if (0 in i and m.index(i) != 0):
            moves.append(m[m.index(i) - 1][i.index(0)])

        if (0 in i and m.index(i) != 3):
            moves.append(m[m.index(i) + 1][i.index(0)])
        
        if (0 in i and i.index(0) != 0):
            moves.append(m[m.index(i)][i.index(0) - 1])

        if (0 in i and i.index(0) != 3):
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
