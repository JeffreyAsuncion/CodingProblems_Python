"""
Given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand 
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You should search for target in nums and if found return its index,
 otherwise return -1.

Example 1:
Input: nums = [6,7,0,1,2,3,4,5], target = 0
Output: 2

Example 2:
Input: nums = [6,7,0,1,2,3,4,5], target = 3
Output: 5

Example 3:
Input: nums = [1], target = 0
Output: -1

Note:

1 <= nums.length < 100
1 <= nums[i] <= 100
All values of nums are unique.
[execution time limit] 4 seconds (py3)

[input] array.integer nums

[input] integer target

[output] integer
"""


"""Brute force"""

def csSearchRotatedSortedArray(nums, target):
    # base case the array is empty
    if not nums:
        return -1
    
    # approach with binary search
    # set a Left and Right Pointer
    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left + right) // 2

        # we found it 
        if target == nums[mid]:
            return mid

        # mid is greater than left:
        if nums[mid] >= nums[left]:
            # target is between L and R
            if nums[left] <= target <= nums[right]:
                # set R to mid -1
                right = mid - 1
            # target is 
            else: 
                # set L to mid + 1
                left = mid + 1
        # otherwise mid is less than L
        else:
            # target is between L and R
            if nums[mid] <= target <= nums[right]:
                # set L to mid + 1
                left = mid + 1
            # target is 
            else:
                # set right = mid - 1
                right = mid - 1

    return -1



#Example 1:
nums = [6,7,0,1,2,3,4,5] 
target = 0
print(csSearchRotatedSortedArray(nums, target))
#Output: 2

#Example 2:
nums = [6,7,0,1,2,3,4,5]
target = 3
print(csSearchRotatedSortedArray(nums, target))
#Output: 5

#Example 3:
nums = [1]
target = 0
print(csSearchRotatedSortedArray(nums, target))
#Output: -1