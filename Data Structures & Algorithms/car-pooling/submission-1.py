class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        heap = []
        rem = capacity

        for num, start, end in trips:
            while heap and heap[-1][0] <= start:
                _, free = heapq.heappop(heap)
                rem += free
            
            if rem >= num:
                heapq.heappush(heap, (end, num))
                rem -= num
            else:
                return False
        
        return True