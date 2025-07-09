# Question: Two Sum
# Problem:

# Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example:

# makefile
# Copy
# Edit
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: nums[0] + nums[1] == 9


def two_sum(nums,target):
    hashTable = {} # value => key
    for i,num in enumerate(nums):
        diff = target  - num
        if diff in hashTable:
            return [hashTable[diff],i]
        hashTable[num] = i
nums = [2,7,11,15]
target = 9
print (two_sum(nums,target))

 