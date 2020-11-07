"""
Let's learn about list comprehensions! 

You are given three integers x, y, z  and
representing the dimensions of a cuboid along 
with an integer n. 
Print a list of all possible coordinates 
given by (i, j, k) on a 3D grid 
where the sum of i + j + k is not equal to  n. Here, . 

0 <= i <= x
0 <= j <= y
0 <= k <= z

Please use list comprehensions rather than multiple loops, as a learning exercise.
"""

### Got it to work with loops,  Next List comprehension
# def ListComp(i, j, k, n):
#     lst = []
#     for x in range(i+1):
#         for y in range(j+1):
#             for z in range(k+1):
#                 if x + y + z != n:
#                     lst.append([x,y,z])
#     return lst

def ListComp(i, j, k, n):
    # result # loop 1 # loop 2 # loop 3 # condition
    lst = [[x,y,z] for x in range(i+1) for y in range(j+1) for z in range(k+1) if (x+y+z) != n]
    return lst

print(ListComp(1,1,1,2))


