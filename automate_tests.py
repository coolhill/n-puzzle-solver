import time
from solver import *

goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

array = [[[1, 2, 3], [0, 6, 8], [5, 4, 7]],
         [[1, 2, 3], [6, 0, 8], [5, 4, 7]],
         [[1, 2, 3], [6, 8, 0], [5, 4, 7]],
         [[1, 2, 0], [6, 8, 3], [5, 4, 7]],
         [[1, 0, 2], [6, 8, 3], [5, 4, 7]],
         [[0, 1, 2], [6, 8, 3], [5, 4, 7]]]

for i in array:
    start_time = time.time()
    print(a_star(Node(i, 3), goal, 3)[0].g)
    print("--- %s seconds ---" % (time.time() - start_time))


