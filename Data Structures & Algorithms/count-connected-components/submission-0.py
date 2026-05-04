class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ret = 0
        
        adjMap = defaultdict(list)

        for u, v in edges:
            adjMap[u].append(v)
            adjMap[v].append(u)
        
        seen = set()

        def dfs(i):
            if i in seen:
                return
            
            seen.add(i)
            for neigh in adjMap[i]:
                dfs(neigh)
            
            return
        
        for i in range(n):
            if i not in seen:
                ret += 1
                dfs(i)

        return ret