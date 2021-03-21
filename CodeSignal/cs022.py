"""
You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.
"""
# https://www.youtube.com/watch?v=4HoHGuAnKro&t=4s

def avoidObstacles(inputArray):
    inputArray.sort()
    # start with mod jump of 2
    jump = 2

        
    # iterate through each val in input array
    index = 0
    while (index < len(inputArray)):
        # if val % jump == 0
        if (inputArray[index] % jump == 0):
            index = -1
            # increment jump because you hit a number
            jump += 1
        
        index += 1
    return jump

inputArray = [5, 3, 6, 7, 9]

print(avoidObstacles(inputArray))
# answer 4.