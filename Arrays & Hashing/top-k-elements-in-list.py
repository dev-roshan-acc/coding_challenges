import heapq
def topKFrequent(nums:list,k:int):
    hashTable = {}
    for num in nums:
        hashTable[num] = hashTable.get(num,0) + 1
    heap = []
    for num,freq in hashTable.items():
        heapq.heappush(heap,(freq,num))
        if len(heap)>k:
            heapq.heappop(heap)
    res = []
    res.extend(heapq.heappop(heap)[1] for _ in range(k))
    return res
    
    



nums = [1,2,2,3,3,3]
k = 2
print(topKFrequent(nums,k))