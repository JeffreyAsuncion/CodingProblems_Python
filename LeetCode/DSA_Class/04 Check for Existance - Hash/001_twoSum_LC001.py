""" 
Example 1: 1. Two Sum

Given an array of integers nums and an integer target, 
return indices of two numbers such that they add up to target. 
You cannot use the same index twice.




"""

def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if complement in d:
            return [i, d[complement]]
        
        d[num] = i

    return [-1,-1]

nums = [5,2,7,10,3,9]
target = 8
print(twoSum(nums,target))