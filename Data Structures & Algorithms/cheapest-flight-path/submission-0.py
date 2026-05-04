class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)

        for frm, to, cost in flights:
            adjList[frm].append((to, cost))
        
        q = deque()
        q.append((0, src))

        minDist = [float('inf')] * n
        minDist[src] = 0

        while q and k >= 0:
            qLen = len(q)

            for i in range(qLen):
                cost, node = q.popleft()

                for nei, dx in adjList[node]:
                    newCost = dx + cost
                    if ((k > 0) or (nei == dst)) and newCost < minDist[nei]:
                        minDist[nei] = newCost
                        q.append((newCost, nei))
            
            k -= 1
        
        return minDist[dst] if minDist[dst] != float('inf') else -1
                    
