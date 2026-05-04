class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjMap = defaultdict(set)

        for u, v in edges:
            adjMap[u].add(v)
            adjMap[v].add(u)
        
        seen = set()

        def dfs(i):
            if i in seen:
                return False
            
            seen.add(i)
            for neigh in adjMap[i]:
                adjMap[neigh].remove(i)
                if not dfs(neigh):
                    return False
        
            return True
        
        return dfs(0) and len(seen) == n
