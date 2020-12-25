"""
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 50.

[output] boolean

true if the characters of the inputString can be rearranged to form a palindrome, false otherwise.
"""

def palindromeRearranging(inputString):
    
    map = {}

    count_middle = 0

    for i in range(len(inputString)):
        if inputString[i] not in  map:
            map[inputString[i]] = 1
        else:
            map[inputString[i]] += 1

    for key, val in map.items():
        if val % 2 != 0:
            count_middle += 1
    if count_middle <= 1:
        return True
            

    
    return False


inputString = "aabb"
print(palindromeRearranging(inputString))# = true.


inputString = "abbcabb"
print(palindromeRearranging(inputString))# = true.

