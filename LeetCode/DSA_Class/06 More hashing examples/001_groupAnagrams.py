"""
Example 1: 49. Group Anagrams

Given an array of strings strs, group the anagrams together.

For example, given strs = ["eat","tea","tan","ate","nat","bat"], return [["bat"],["nat","tan"],["ate","eat","tea"]].
"""

from collections import defaultdict

# def groupAnagrams(s):
#     groups = defaultdict(list)
#     for s in strs:
#         key = "".join(sorted(s))
#         print(key)
#         groups[key].append(s)
    
#     return groups.values()

def groupAnagrams(s):
    groups = defaultdict(list)

    for s in strs:
        print(s, sorted(s), "".join(sorted(s)))
        key = "".join(sorted(s))
        groups[key].append(s)
    print(groups.values())
    return groups.values()

strs = ["eat","tea","tan","ate","nat","bat"]
# return [["bat"],["nat","tan"],["ate","eat","tea"]].
print(groupAnagrams(strs))