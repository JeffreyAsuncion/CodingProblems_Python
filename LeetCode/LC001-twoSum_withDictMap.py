"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and 
you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

arr1 = [1, 3, 5, 6]
target1 = 8

arr2 = [4, 7, 2, 8]
target2 = 12


def twoSum(nums, target):
    # create a dictionary to hold the values
    values = dict()

    # iterate thru nums
    for index, element in enumerate(nums):
        
        comp = target - element

        # check to see if comp is in the dictionary
        if comp in values:
            # return index of comp and index
            return[values[comp], index]
        # add the element to dictionary
        values[element] = index
    # return empty list
    return []

print(twoSum(arr1, target1))
print(twoSum(arr2, target2))
