import heapq
def topKFrequent(nums:list,k:int):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num,0) + 1

    heap =[]
    for num in freq:
        heapq.heappush(heap,(freq,num))
        if len(heap)>k:
            heapq.heappop(heap)

    res = []
    res.extend(heapq.heappop(heap)[1] for _ in range(k))
    return res



nums = [1,2,2,3,3,3]
k = 2
print(topKFrequent(nums,k))