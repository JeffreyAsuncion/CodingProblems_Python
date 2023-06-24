
nums = [3,6,2,8,1,4,1,5]

prefix = [nums[0]]

for i in range(1, len(nums)):
    prefix.append(nums[i] + prefix[len(prefix) - 1])

print(prefix)