"""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
isLucky(n) = true;
For n = 239017, the output should be
isLucky(n) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

A ticket number represented as a positive integer with an even number of digits.

Guaranteed constraints:
10 ≤ n < 106.
"""

    
def isLucky(n):
    ticket = str(n)
    total_length = len(ticket)
    half1 = []
    half2 = []
    halfOneStr = ticket[:total_length//2]
    halfTwoStr = ticket[total_length//2:]
    print(halfOneStr, halfTwoStr)
    for i in halfOneStr:
        half1.append(int(i))
    for i in halfTwoStr:
        half2.append(int(i))
    return sum(half1) == sum(half2)

n1 = 1230
print(isLucky(n1))# = true;
n2 = 239017
print(isLucky(n2))# = false.


