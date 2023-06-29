""" 
Example 2: 2351. First Letter to Appear Twice
using a set

Given a string s, return the first character to appear twice. 
It is guaranteed that the input will have a duplicate character.
"""

def repeatedCharacter(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        else:
            seen.add(char)
    return False

s = 'abba'
print(repeatedCharacter(s))