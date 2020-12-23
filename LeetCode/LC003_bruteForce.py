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

def allUnique(s, start, end):
         
        seenStr = ''
        for i in range(start, end):
            char = s[i]
            # check if char has been seen already in seenStr
            if char in seenStr:
                # return False - char is not unique
                return False
            else:
                seenStr += char
        # return True - char is unique
        return True



def lengthOfLongestSubstring(s: str) -> int:
    # base case where s is empty string
    if s == "":
        # return length of 0
        return 0
    
    longest = 0
    for i in range(len(s)):
        j = i + 1
        # corrected the range to len(s) + 1 and works on edge cases but TimesOut longer strings
        # O(n^3) need to optimize        
        for j in range(len(s)+1):   # range == len(s) + 1 to correct for j = i + 1
            if allUnique(s,i,j):
                # ans is the max value of ans vs j -i 
                longest = max(longest, j-i)
    return longest

            

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