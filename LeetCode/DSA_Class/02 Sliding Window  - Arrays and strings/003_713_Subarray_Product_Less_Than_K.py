""" 
713. Subarray Product Less Than K.
Given an array of positive integers nums and an integer k, 
return the number of subarrays where the product of all the elements in the subarray is strictly less than k.

For example, given the input nums = [10, 5, 2, 6], k = 100, the answer is 8. 
The subarrays with products less than k are:

[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]

To demonstrate the property we have just learned, 
let's look at the example in the description. When we reach index 2, 
the product becomes too large, so we need to remove the leftmost element 10. 
Now, the window is valid, and it has a length of 2. 
That means that there are 2 valid subarrays that end here ([2] and [5, 2]).

Recall that in the previous examples, 
we updated the answer (longest length) after the while loop, 
when the window must be valid. Here, we can add the current size of the window to our answer instead. 
The constraint that determines if a window is valid is that the product is less than k.

Additionally, note that if k <= 1 we can never have any valid windows, so we can just return 0 immediately.

"""


def numSubarrayProductLessThanK(nums, k):
    ans = left = 0
    curr = 1
    
    for right in range(len(nums)):
        # each element add to curr window
        curr *= nums[right]
        
        # check condition broken
        while curr >= k:
            # remove from window 
            curr /= nums[left]
            left += 1
        
        # since the number of valid subarrays is equal to the length of the subarray
        # white board to see.
        ans += right - left + 1
    
    return ans


if __name__ == '__main__':
    nums = [10, 5, 2, 6]
    k = 100
    output = 8 
    
    if numSubarrayProductLessThanK(nums,k) == output:
        print('Validated')
    else:
        print("back to work! :-(")