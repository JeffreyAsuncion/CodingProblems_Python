"""
Given an int n, 
return the absolute difference between n and 21, 
except return double the absolute difference if n is over 21.


diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
"""

def diff21(n):
    # if n is 21 or under return the abs difference between n and 21
    if n <= 21:
        return abs(n-21)
    #if n is over 21, return double the abs difference
    else:
        return 2 * abs(n-21)



print(diff21(19))
print(diff21(10))
print(diff21(21))
