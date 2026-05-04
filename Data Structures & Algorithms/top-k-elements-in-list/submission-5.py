class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret = []
        count = {}

        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        countList = []

        for n, v in count.items():
            heapq.heappush(countList, (v, n))
            if len(countList) > k:
                heapq.heappop(countList)
        
        return [y for _, y in countList]
