class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = defaultdict(int)

        for n in nums:
            countMap[n] += 1
        
        minHeap = []

        for n, v in countMap.items():
            heapq.heappush(minHeap, (v, n))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return [n for _, n in minHeap]
