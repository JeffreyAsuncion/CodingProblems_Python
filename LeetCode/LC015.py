"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
"""


def threeSum(nums):
    # results list
    results = []
    # sort list in ascending order
    nums.sort()
    # find the length of the list
    length = len(nums)
    
    # loop thru the list
    for i in range(length-2):  # -2 to account for the two pointers Left and Right
        # must not contain duplicate triplets
        if i > 0 and nums[i] == nums[i-1]:
            # just keep going
            continue
        Left = i + 1
        Right = length - 1
        
        while Left < Right:
            total = nums[i] + nums[Left] + nums[Right]
            # if total is less that 0, move Left add 1
            if total < 0:
                Left = Left + 1
                print("Left")
            # if total is greater than 0, move Right minus 1
            elif total > 0:
                Right = Right - 1
                print("Right")
            # then the total is 0
            else:
                # append all three values to the results
                results.append([nums[i],nums[Left],nums[Right]])
                print("Got it!")
                # This is a check to make sure that the Left and Right are not part of a Triplet
                # check if Left and Left+1 are not part of a Triplet
                while Left < Right and nums[Left] == nums[Left+1]:
                    Left = Left + 1 
                # check if Right and Right-1 are not part of a Triplet
                while Left < Right and nums[Right] == nums[Right -1]:
                    Right = Right -1
                # otherwise
                Left = Left + 1
                Right = Right -1
            # i += 1
    return results



# Input: 
nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

print(threeSum(nums))