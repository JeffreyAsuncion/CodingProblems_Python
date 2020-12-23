"""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s1

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ s1.length < 15.

[input] string s2

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ s2.length < 15.

[output] integer
"""

def commonCharacterCount(s1, s2):
    common_count = 0
    seen1 = {}
    seen2 = {}
    for i in s1:
        if i not in seen1:
            seen1[i] = 1
        else:
            seen1[i] += 1
            
    for i in s2:
        if i not in seen2:
            seen2[i] = 1
        else:
            seen2[i] += 1
    
    print(seen1)
    print(seen2)
    for key, val in seen1.items():
        if key in seen2:
            common_count += min(seen1[key], seen2[key])
            print(key)
    
    
    return common_count


s1 = "aabcc" 
s2 = "adcaa"
print(commonCharacterCount(s1, s2))# = 3.
