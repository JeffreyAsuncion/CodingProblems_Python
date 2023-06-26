def removeDuplicates(nums):
    i, j = 0, 0
    while j < len(nums):
        if nums[j] == nums[i]:
            j += 1
        else:
            i += 1 
            nums[i] = nums[j]
    print(type(i+1))
    print(nums[:i+1])
    return i+1

nums = [1,1,2]
print(removeDuplicates(nums))