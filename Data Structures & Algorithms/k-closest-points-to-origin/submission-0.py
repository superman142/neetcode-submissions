class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        def dist(x, y):
            return math.sqrt(x*x + y*y)

        for x, y in points:
            maxHeap.append((dist(x, y), x, y))
        
        heapq.heapify(maxHeap)
        ret = []

        while len(ret) < k:
            _, x, y = heapq.heappop(maxHeap)
            ret.append([x, y])

        return ret
