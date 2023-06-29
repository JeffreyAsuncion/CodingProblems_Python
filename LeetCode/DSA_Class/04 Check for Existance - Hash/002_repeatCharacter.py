""" 
Example 2: 2351. First Letter to Appear Twice

Given a string s, return the first character to appear twice. 
It is guaranteed that the input will have a duplicate character.
"""

def repeatedCharacter(s):
    seen = {}
    for i in range(len(s)):
        if s[i] in seen:
            return s[i]
        else:
            seen[s[i]] = 1
    return False

s = 'abba'
print(repeatedCharacter(s))