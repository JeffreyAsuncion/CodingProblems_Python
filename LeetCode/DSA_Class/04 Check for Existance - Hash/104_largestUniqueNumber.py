"""
Largest Unique Number

Solution
Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.

 

Example 1:

Input: nums = [5,7,3,9,4,9,8,3,1]
Output: 8
Explanation: The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it is the answer.
Example 2:

Input: nums = [9,9,8,8]
Output: -1
Explanation: There is no number that occurs only once.
 

Constraints:

1 <= nums.length <= 2000
0 <= nums[i] <= 1000
"""

def largestUniqueNumber(nums):
    ans = 0
    d = {}
    ans_list = []
    for num in nums:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1

    for key, val in d.items():
        if val == 1:
            ans_list.append(key)

    if len(ans_list) == 0:
        return -1
    return sorted(ans_list)[-1]

nums = [5,7,3,9,4,9,8,3,1]
# Output: 8
print(largestUniqueNumber(nums))