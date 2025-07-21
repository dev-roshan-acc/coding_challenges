# K Closest Points to Origin
# You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. You are also given an integer k.

# Return the k closest points to the origin (0, 0).

# The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).

# You may return the answer in any order.
from typing import List
import heapq
from checker import OutputChecker


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    distances = [(x**2 + y**2, [x, y]) for x, y in points]
    heapq.heapify(distances)
    result = [] #an empty array for storing closest points
    for _ in range(k):
        _,point = heapq.heappop(distances)
        result.append(point)

    return result


testChecker = OutputChecker(kClosest)
points, k = [[0, 2], [2, 0], [2, 2]], 2  
expectedOutput = [[0,2],[2,0]]
testChecker.run_test((points, k),expectedOutput)


points, k = [[1, 1], [3, 4], [2, -1]], 2  
expectedOutput = [[1,1],[2,-1]]
testChecker.run_test((points, k),expectedOutput)


points, k = [[5, 5], [1, 2], [0, 0]], 1  
expectedOutput = [[0,0]]
testChecker.run_test((points, k),expectedOutput)

points, k = [[-2, -4], [3, 3], [1, 0], [0, 2]], 3  
expectedOutput = [[1,0],[0,2],[3,3]]
testChecker.run_test((points, k),expectedOutput)

points, k = [[7, 8], [2, 2], [1, 0], [3, 3]], 2  
expectedOutput = [[1,0],[2,2]]
testChecker.run_test((points, k),expectedOutput)
