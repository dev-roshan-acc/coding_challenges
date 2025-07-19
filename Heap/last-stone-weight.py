# Last Stone Weight
# Solved 
# You are given an array of integers stones where stones[i] represents the weight of the ith stone.

# We want to run a simulation on the stones as follows:

# At each step we choose the two heaviest stones, with weight x and y and smash them togethers
# If x == y, both stones are destroyed
# If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# Continue the simulation until there is no more than one stone remaining.

# Return the weight of the last remaining stone or return 0 if none remain.


from typing import List
import heapq

def lastStoneWeight( stones: List[int]) -> int:
    stones = [-s for s in stones]
    heapq.heapify(stones)
    while len(stones)>1:
        x = heapq.heappop(stones)
        y = heapq.heappop(stones)
        if x<y:
            heapq.heappush(stones,-(y-x))
    stones.append(0)
    return abs(stones[0])

stones = [2, 3, 6, 2, 4]   # example 1  output = 1
print(f"Output: {lastStoneWeight(stones)}")

stones = [1, 1, 1, 1]      # example 2  output = 0
print(f"Output: {lastStoneWeight(stones)}")

stones = [10]              # example 3  output = 10
print(f"Output: {lastStoneWeight(stones)}")

stones = [4, 4, 4, 3]     # example 4  output = 1
print(f"Output: {lastStoneWeight(stones)}")

stones = [7, 6, 7, 6, 9]  # example 5  output = 3
print(f"Output: {lastStoneWeight(stones)}")


        
        