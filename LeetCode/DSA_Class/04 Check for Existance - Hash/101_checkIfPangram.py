""" 
Check if the Sentence Is Pangram

Solution
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, 
return true if sentence is a pangram, or false otherwise.

 

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false
"""

def checkIfPangram(sentence):    
    dict_letter = {}
    # print(len(sentence))
    for i in range(len(sentence)):
        if sentence[i] in dict_letter:
            dict_letter[sentence[i]] += 1
        else:
            dict_letter[sentence[i]] = 1
    
    return len(dict_letter) == 26

sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
print(checkIfPangram(sentence))
sentence = "leetcode"
# Output: false
print(checkIfPangram(sentence))