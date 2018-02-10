import math
import collections

def is_valid_sudoku(partial_assignment):
    region_size = int(math.sqrt(len(partial_assignment)))
    return max(
            collections.Counter(k
                for i, row in enumerate(partial_assignment)
                for j, c in enumerate(row)
                if c!= 0
                for k in ((i,str(c)), (str(c), j),
                    (i / region_size, j / region_size,
                        str(c)))).values(),
                    defualt = 0) <= 1
