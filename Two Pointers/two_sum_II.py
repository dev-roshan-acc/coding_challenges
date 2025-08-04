# Two Integer Sum II
# Solved 
# Given an array of integers numbers that is sorted in non-decreasing order.

# Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

# There will always be exactly one valid solution.

# Your solution must use 
# O
# (
# 1
# )
# O(1) additional space.

# Example 1:

# Input: numbers = [1,2,3,4], target = 3

# Output: [1,2]
# Explanation:
# The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].

# Constraints:

# 2 <= numbers.length <= 1000
# -1000 <= numbers[i] <= 1000
# -1000 <= target <= 1000

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    left,right = 0 , len(nums)-1
    
    while left<right:
        current = nums[left] + nums[right]
        if target<current:
            right-=1
        elif target>current:
            left+=1
        else: return [left+1,right+1]
        

nums, target = [1, 2, 3, 4], 3  # example 1 output = [1, 2]
print(twoSum(nums, target))

nums, target = [2, 7, 11, 15], 9  # example 2 output = [1, 2]
print(twoSum(nums, target))

nums, target = [1, 3, 5, 7, 9], 12  # example 3 output = [3, 5]
print(twoSum(nums, target))

nums, target = [0, 0, 3, 4], 0  # example 4 output = [1, 2]
print(twoSum(nums, target))

nums, target = [1, 2, 3, 4, 5, 6], 11  # example 5 output = [5, 6]
print(twoSum(nums, target))







