"""
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string inputArray

A non-empty array.

Guaranteed constraints:
1 ≤ inputArray.length ≤ 10,
1 ≤ inputArray[i].length ≤ 10.

[output] array.string

Array of the longest strings, stored in the same order as in the inputArray.
"""


def allLongestStrings(inputArray):
    max_length = 0
    resultStr = []
    for i in range(len(inputArray)):
        if len(inputArray[i]) >= max_length:
            max_length = len(inputArray[i])
    for i in range(len(inputArray)):
        if len(inputArray[i]) == max_length:        
            resultStr.append(inputArray[i])
    return resultStr



inputArray = ["aba", "aa", "ad", "vcd", "aba","eeeeeeeeeeeeeee"]
print(allLongestStrings(inputArray)) # = ["aba", "vcd", "aba"].
