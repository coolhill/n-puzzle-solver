end = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
start = [1, 2, 3, 4, 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
bad = [0, 3, 4, 7, 8, 11, 12, 15]


openNodes = [[start]]
closedNodes = []

# Solve using A* algoritm
def solve(current, end):
    left = current.index(0)-1
    right = current.index(0)+1
    up = current.index(0)-4
    down = current.index(0)+4
    grannar = [left, right, up, down]

    # Excludes unwanted grannar
    for granne in grannar:
        if granne > 16 or granne < 0 or ((bad.count(granne) == 1 and abs(current.index(0)-granne) == 1)):
            grannar.remove(granne)

    # Generate successor-nodes (by the 0's grannar)
    for granne in grannar:
        #new = current
        new = [1, 2, 3, 4, 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] #used for debugging purposes
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
