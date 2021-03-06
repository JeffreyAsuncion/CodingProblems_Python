"""
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers 
within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function 
returns 0 when the reversed integer overflows.



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0


Constraints:

-231 <= x <= 231 - 1

"""



def reverse(x):
    """
    :type x: int
    :rtype: int
    """


    new_str = str(x)
    i = 1
    rev_str = new_str[::-1]
    if rev_str[-1] == "-":
        rev_str = rev_str.strip("-")
        i = -1
    if (int(rev_str)>=2**31):
        return 0
    return (int(rev_str)) * i



print(reverse(12345))
print(reverse(-54321))
print(reverse(852))
