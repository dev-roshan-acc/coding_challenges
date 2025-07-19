
from typing import List
import heapq


def findKthLargest( nums: List[int], k: int) -> int:
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap,num)
        if len(min_heap)>k:
            heapq.heappop(min_heap)
    
    return min_heap[0]

nums, k = [2, 3, 1, 5, 4], 2  # Output = 4
print(f"Output: {findKthLargest(nums, k)}")

nums, k = [7, 10, 4, 3, 20, 15], 3  # Output = 10
print(f"Output: {findKthLargest(nums, k)}")

nums, k = [1, 1, 1, 1], 2  # Output = 1
print(f"Output: {findKthLargest(nums, k)}")

nums, k = [9, 8, 3, 6, 5, 2], 1  # Output = 9
print(f"Output: {findKthLargest(nums, k)}")

nums, k = [5, 3, 2, 4, 1], 5  # Output = 1
print(f"Output: {findKthLargest(nums, k)}")
