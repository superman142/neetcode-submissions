class DSU:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        
        return self.parent[i]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        
        self.size[pu] += self.size[pv]
        self.parent[pv] = pu
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        graph = DSU(len(points))

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[j][1] - points[i][1]) + abs(points[j][0] - points[i][0])
                edges.append([dist, i, j])
        
        heapq.heapify(edges)
        edgesUsed = 0

        ret = 0

        while edgesUsed < len(points) - 1:
            dist, u, v = heapq.heappop(edges)

            if graph.union(u, v):
                edgesUsed += 1
                ret += dist
        
        return ret

        