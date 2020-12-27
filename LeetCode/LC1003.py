"""
You are given a parentheses sequence, check if it's regular.
Example
For s = "()()(())", the output should be
validParenthesesSequence(s) = true;
For s = "()()())", the output should be
validParenthesesSequence(s) = false.
Input/Output
[execution time limit] 4 seconds (py3)
[input] string s
A string, consisting only of '(' and ')'.
Guaranteed constraints:
0 ≤ s.length ≤ 105.
[output] boolean
true is the sequence is regular and false otherwise.
"""

"""This just counts them but does not match them"""
# def validParenthesesSequence(s):
#     result = False
#     if s.count('(') == s.count(')'):
#         result = True

#     return result

"""Leet code help"""
# Algotirithm
# 1. Initialize a stack S
# 2. Iterate over each character in the string
# 3. If we encounter an open bracket, push it onto the stack
# 4. If we encounter a closing bracket, check the top of the stack
#       a.  If the top of the stack is an open bracket of the same type, continue
#       b.  Else, return False

def validParenthesesSequence(s):
    # stack to hold the values we see
    stack = []
    # a hash map to help us match the valid parentheses
    mapping = {")": "("}

    # loop thru the input string
    for char in s:

        # check if the char is in the mapping
        if char in mapping:
            # if stack is still full
            if stack:
                # pop last element off stack
                top_elem = stack.pop()
            # otherwise stack is empty
            else:
                # pass a filler to check map
                top_elem = "#" # note this could be any symbol not a  bracket or parens
            
            # check if element popped matches
            if mapping[char] != top_elem:
                return False
        # otherwise not in map
        else:
            # adding to stack
            stack.append(char)
    
    return not stack # if the stack it empty, then it is even AND PARENS are Valid

            


s = "()()(())"
print(validParenthesesSequence(s)) # = true;

s = "()()())"
print(validParenthesesSequence(s)) # = false.