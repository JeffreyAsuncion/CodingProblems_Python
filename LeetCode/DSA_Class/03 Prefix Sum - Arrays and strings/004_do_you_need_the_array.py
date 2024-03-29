"""
Do we need the array?
In this problem, the order in which we need to access prefix is incremental: 
to find leftSection, we do prefix[i] as i increments by 1 each iteration.

As such, to calculate leftSection we don't actually need the array. 
We can just initialize leftSection = 0 and 
then calculate it on the fly by adding the current element to it at each iteration.

What about rightSection? 
By definition, the right section contains all the numbers in the array 
that aren't in the left section. 
Therefore, we can pre-compute the sum of the entire input as total, 
then calculate rightSection as total - leftSection.

We are still using the concept of a prefix sum as each value of leftSection 
represents the sum of a prefix. 
We have simply replicated the functionality using an integer instead of an array.
"""


"""
We have improved the space complexity to O(1), which is a great improvement.
"""

# class Solution:
#     def waysToSplitArray(self, nums: List[int]) -> int:
#         ans = left_section = 0
#         total = sum(nums)

#         for i in range(len(nums) - 1):
#             left_section += nums[i]
#             right_section = total - left_section
#             if left_section >= right_section:
#                 ans += 1

#         return ans
    
def waysToSplitArray(nums):
    ans = L = 0
    total = sum(nums)

    for i in range(len(nums)-1):
        L += nums[i]
        R = total - L
        if L > R:
            ans += 1

    return ans


if __name__ == '__main__':
    nums = [10,4,-8,7]
    ouput = 2

    print(waysToSplitArray(nums))