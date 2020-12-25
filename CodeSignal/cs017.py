"""
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer inputArray

Guaranteed constraints:
3 ≤ inputArray.length ≤ 105,
-105 ≤ inputArray[i] ≤ 105.

[output] integer

The minimal number of moves needed to obtain a strictly increasing sequence from inputArray.
It's guaranteed that for the given test cases the answer always fits signed 32-bit integer type.
"""

def arrayChange(inputArray):
    moves = 0

    print(inputArray)
    
    for i in range(len(inputArray)-1):
        if inputArray[i] >= inputArray[i+1]:
            # find the difference 
            diff = inputArray[i] - inputArray[i+1] + 1
            # add diff to moves
            moves += diff
            # this resets the array
            inputArray[i+1] += diff


            print(inputArray)

 
    return moves

inputArray = [1, 1, 1]
print(arrayChange(inputArray))# = 3.

inputArray = [-1000, 0, -2, 0]
print(arrayChange(inputArray))# -2992
