class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = defaultdict(int)

        for n in nums:
            countMap[n] += 1
        
        maxHeap = [(-v, n) for n, v in countMap.items()]
        heapq.heapify(maxHeap)

        ret = []

        while len(ret) < k:
            _, n = heapq.heappop(maxHeap)
            ret.append(n)
        
        return ret
