
# Longest Consecutive Sequence
# Solved 
# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

# You must write an algorithm that runs in O(n) time.


from checker import OutputChecker


def longestConsecutive( nums: list[int]) -> int:
    # convert nums array into set 
    numSet = set(nums)
    longest = 0
    
    for num in numSet:
        # start of a sequence means {2,3,4,5,6} check if the set has 1 or not
        if num - 1 not in numSet:
            # for counting total nums in set which cnsecutive sequence
            len = 1
            while num + len in numSet:
                len += 1
            longest = max(longest,len)
    return longest


testChecker = OutputChecker(longestConsecutive)

testChecker.run_test(([100, 4, 200, 1, 3, 2]), 4, "Test Case 1")      
testChecker.run_test(([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9, "Test Case 2") 
testChecker.run_test(([1, 2, 0, 1]), 3, "Test Case 3")                  
testChecker.run_test(([]), 0, "Test Case 4")                            
testChecker.run_test(([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]), 7, "Test Case 5") 
