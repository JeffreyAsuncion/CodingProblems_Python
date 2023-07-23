"""
Maximum Number of Balloons

Solution
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.
"""
from collections import Counter

def maxNumberOfBalloons(s):
    ans = len(s)
    s_dict = {}
    balloon = Counter('balloon')
    
    text = Counter(s)

    for c in balloon:
        ans = min(ans, text[c] // balloon[c])
    print(balloon)
    # print(s_dict)
    return ans

    return ans


text = 'balloons'
print(maxNumberOfBalloons(text))


text = "loonbalxballpoon"
print(maxNumberOfBalloons(text))
# 'Output: 2

text = "leetcode"
print(maxNumberOfBalloons(text))
# Output: 0