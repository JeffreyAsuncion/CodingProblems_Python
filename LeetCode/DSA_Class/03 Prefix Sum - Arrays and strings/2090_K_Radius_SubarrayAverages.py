"""
# https://www.youtube.com/watch?v=aiHxMvMFI00
"""

def getAverages(nums, k):
    # When a single element is considered then its average will be the number itself only.
    if k == 0:
        return nums

    n = len(nums)
    averages = [-1] * n

    # Any index will not have 'k' elements in it's left and right.
    if 2 * k + 1 > n:
        return averages

    # Generate 'prefix' array for 'nums'.
    # 'prefix[i + 1]' will be sum of all elements of 'nums' from index '0' to 'i'.
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]
        
    # We iterate only on those indices which have atleast 'k' elements in their left and right.
    # i.e. indices from 'k' to 'n - k'
    for i in range(k, n - k):
        leftBound, rightBound = i - k, i + k
        subArraySum = prefix[rightBound + 1] - prefix[leftBound]
        print(rightBound+1,leftBound,subArraySum)

        average = subArraySum // (2 * k + 1)
        averages[i] = average

    return averages

nums = [7,4,3,9,1,8,5,2,6]
k = 3

print(getAverages(nums,k))