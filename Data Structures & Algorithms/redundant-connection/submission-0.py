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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = DSU(len(edges) + 1)

        for u, v in edges:
            if not graph.union(u, v):
                return [u, v]
        
        return []




        