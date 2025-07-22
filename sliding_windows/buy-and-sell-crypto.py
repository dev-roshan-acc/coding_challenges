
# Best Time to Buy and Sell Stock
# Solved 
# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

# Example 1:

# Input: prices = [10,1,5,6,7,1]

# Output: 6
# Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

# Example 2:

# Input: prices = []

# Output: 0
# Explanation: No profitable transactions can be made, thus th10,8,7,5,2e max profit is 0.

# Constraints:

# 1 <= prices.length <= 100
# 0 <= prices[i] <= 100


from typing import List
from checker import OutputChecker


def maxProfit(prices: List[int]) -> int:
    maxP = 0
    l,r  = 0,1
    while r<len(prices):
        if prices[r]>prices[l]:
            profit = prices[r] - prices[l]
            maxP = max(profit,maxP)
        else:
            l=r
        r+=1
    return maxP


testChecker = OutputChecker(maxProfit)


testChecker.run_test(([10, 1, 5, 6, 7, 1]), 6, "Test Case 1")
testChecker.run_test(([7, 6, 4, 3, 1]), 0, "Test Case 2")
testChecker.run_test(([1, 2, 3, 4, 5]), 4, "Test Case 3")
testChecker.run_test(([3, 2, 6, 5, 0, 3]), 4, "Test Case 4")
testChecker.run_test(([8, 9, 1, 2, 10, 3]), 9, "Test Case 5")
    