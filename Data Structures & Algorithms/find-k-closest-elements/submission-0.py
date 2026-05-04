class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for i, n in enumerate(arr):
            heapq.heappush(heap, ( -abs(n - x), -n))
            if len(heap) > k:
                heapq.heappop(heap)

        ret = [-x for _, x in heap]
        
        ret.sort()
        return ret