"""
You are given a 2d grid of `"1"`s and `"0"`s that represents a "map". The
`"1"`s represent land and the `"0"s` represent water.
You need to write a function that, given a "map" as an argument, counts the
number of islands. Islands are defined as adjacent pieces of land that are
connected horizontally or vertically. You can also assume that the edges of the
map are surrounded by water.
Example 1:
Input: grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
Output: 1
Example 2:
Input: grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
Output: 3
"""

"""

Islands Problem
or
Connected Components

"""

from collections import deque

def numIslands(grid):
    # Your code here
    # if there is no grid or the grid is empty then
    if grid is None or len(grid) == 0:
        # return zero
        return 0

    # store some lens and an island count
    nr = len(grid)
    nc = len(grid[0])
    island_count = 0

    # iterate over each row
    for row in range(nr):
        # iterate over each col
        for col in range(nc):
            # check if our grid at [row][col] is "1"
            if grid[row][col] == "1":
                # it is an island
                # increment the number of islands
                island_count += 1
                # mark it as visited, change it to "0"
                grid[row][col] = "0"

                # set up a queue of neighbors
                neighbors = deque()
                # append row * number_col + col to neighbors
                # this makes it a 1-D array
                neighbors.append(row * nc + col)

                # while there are still neighbors
                while len(neighbors) != 0:
                    # set up an id based on a current neighbor and REMOVE the neighbor
                    id = neighbors.popleft()

                    # this remake it into a 2-D array
                    # set the row
                    row = id // nc 
                    # set the col
                    col = id % nc

                    # check all the directions
                    # for connected components

                    # check up
                    if row-1 >=0 and grid[row-1][col] == "1":
                        neighbors.append((row-1) * nc + col)
                        grid[row-1][col] = "0"

                    # check down
                    if row+1 <nr and grid[row+1][col] == "1":
                        neighbors.append((row+1) * nc + col)
                        grid[row+1][col] = "0"

                    # check left
                    if col-1 >=0 and grid[row][col-1] == "1":
                        neighbors.append((row) * nc + (col-1))
                        grid[row][col-1] = "0"

                    # check right
                    if col+1 < nc and grid[row][col+1] == "1":
                        neighbors.append((row) * nc + (col+1))
                        grid[row][col+1] = "0"

    # return island count
    return island_count







grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]

print(numIslands(grid))

grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

print(numIslands(grid))