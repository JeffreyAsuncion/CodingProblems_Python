"""
3. Longest Substring Without Repeating Characters

Given a string s, 
find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
Input: s = ""
Output: 0
 
Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

def lengthOfLongestSubstring(s: str) -> int:
    # base case of 0
    if len(s) == 0:
        return 0

    # map datastructure
    map = {}
    max_length = 0
    start = 0

    # iterate thru string
    for i in range(len(s)):
        # check if s[i] in map and if the start point is LTE s[i] index
        if s[i] in map and start <= map[s[i]]:
            # increment the start point
            start = map[s[i]] + 1
        # otherwise check the length 
        else:
            # return the larger length
            max_length = max(max_length, i - start + 1)
        
        # add to the map    
        map[s[i]] = i
        
    # return result
    return max_length







            

# Example 1:
s1 = "abcabcbb"
print(lengthOfLongestSubstring(s1)) # Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
s2 = "bbbbb"
print(lengthOfLongestSubstring(s2))#Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
s3 = "pwwkew"
print(lengthOfLongestSubstring(s3))#Output: 3
# Explanation: The answer is "wke", with the length of 3.

# Example 4:
s4 = ""
print(lengthOfLongestSubstring(s4))# Output: 0

# Example 5:
s5 = "aab"
print(lengthOfLongestSubstring(s5))# Output: 2