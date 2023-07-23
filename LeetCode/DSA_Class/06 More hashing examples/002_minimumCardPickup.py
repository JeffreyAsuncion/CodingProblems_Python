"""
Example 2: 2260. Minimum Consecutive Cards to Pick Up

Given an integer array cards, 
find the length of the shortest subarray that contains at least one duplicate. 
If the array has no duplicates, return -1.

We can actually solve this problem using a sliding window, 
but let's take a look at another approach that has more emphasis on a hash map. 
This question is equivalent to: 
what is the shortest distance between any two of the same element? 
If we go through the array and use a hash map to record the indices for every element, 
we can iterate over those indices to find the shortest distance. 
For example, given cards = [1, 2, 6, 2, 1], 
we would map 1: [0, 4], 2: [1, 3], and 6: [2]. 
Then we can iterate over the values and 
see that the minimum difference can be achieved from picking up the 2s.
"""

# from collections import defaultdict

# def minimumCardPickup(cards):
#     dic = defaultdict(list)
#     for i in range(len(cards)):
#         dic[cards[i]].append(i)
        
#     ans = float("inf")
#     for key in dic:
#         arr = dic[key]
#         for i in range(len(arr) - 1):
#             ans = min(ans, arr[i + 1] - arr[i] + 1)
    
#     return ans if ans < float("inf") else -1
from collections import defaultdict

def minimumCardPickup(cards):
    dic = defaultdict(list)
    for i in range(len(cards)):
        dic[cards[i]].append(i)
    ans = float('inf')
    for key, value in dic.items():
        if len(value) == 2:
            ans = min(ans, value[1]-value[0])
    return ans
    

    return


cards = [1, 2, 6, 2, 1]
print(minimumCardPickup(cards))
# we would map 1: [0, 4], 2: [1, 3], and 6: [2]. 