class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        def dist(x, y):
            return math.sqrt(x**2 + y**2)    

        for x, y in points:
            heapq.heappush(maxHeap, (-dist(x, y), x, y))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        return [[x, y] for _, x, y in maxHeap]