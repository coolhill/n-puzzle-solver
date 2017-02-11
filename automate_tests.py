import time
from solver import *

goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

size = 3

for i in range(10,50,10):

    start_time = time.time()
    start = shuffle(goal, size, i).q

    for a in a_star(Node(start, size), goal, size):
        for b in a.q:
            print(b)
        print("")
        
    print("--- %s seconds ---" % (time.time() - start_time))

