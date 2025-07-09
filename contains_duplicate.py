# Contains Duplicate
# Solved 
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true

# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false


def hasDuplicate(nums):
    hashTable = {}
    for (x,num) in enumerate(nums):
        if num in hashTable:
            return True
        hashTable[num] = x 
    return False


nums1 = [1, 2, 3, 3]
print ('example1: ',hasDuplicate(nums1))

nums2 = [1, 2, 3, 4]
print ('example2: ',hasDuplicate(nums2))
    