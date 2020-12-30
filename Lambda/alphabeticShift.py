"""
Given a string, your task is to replace 
each of its characters by the next one in the English alphabet; 
i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be 
alphabeticShift(inputString) = "dsbaz".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A non-empty string consisting of lowercase English characters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 1000.

[output] string

The resulting string after replacing each of its characters.
"""

def alphabeticShift(inputString):
    abc = "abcdefghijklmnopqrstuvwxyz"
    new_str = ""
    for letter in inputString:
        i = abc.index(letter)

        x = i + 1
        if x == 26:
            x = 0
        new_letter = abc[x]
        new_str += new_letter
    
    return new_str




inputString = "crazy" 
print(alphabeticShift(inputString)) # = "dsbaz".