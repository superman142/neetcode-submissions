class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)

        for u, v, t in times:
            adjList[u].append((v, t))
        
        heap = [(0, k)]

        seen = set()
        tmax = 0

        while len(seen) != n and heap:
            t, u = heapq.heappop(heap)

            if u in seen:
                continue
            
            seen.add(u)
            tmax = t

            for nei, tu in adjList[u]:
                heapq.heappush(heap, (t + tu, nei))
        
        return tmax if len(seen) == n else -1
            


