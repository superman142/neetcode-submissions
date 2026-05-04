class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        seen = set()

        def dfs(i):
            seen.add(i)

            for nei in adjList[i]:
                if nei not in seen:
                    dfs(nei)
        
        ret = 0

        for i in range(n):
            if i not in seen:
                ret += 1
                dfs(i)
        
        return ret

