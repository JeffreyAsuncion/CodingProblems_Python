"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""

def groupAnagrams(strs):
    
    map = {}
    
    for word in strs:
        sortedWord = "".join(sorted(word))
        
        if sortedWord not in map:
            map[sortedWord] = [word]
        else:
            map[sortedWord].append(word)
            
    
    results = []
    
    for item in map.values():
        results.append(item)
        print(results)
        
    return results



strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


strs = [""]
print(groupAnagrams(strs))
# Output: [[""]]


strs = ["a"]
print(groupAnagrams(strs))
# Output: [["a"]]