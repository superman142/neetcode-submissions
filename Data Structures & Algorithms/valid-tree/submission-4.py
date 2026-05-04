class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
            
        adjList = defaultdict(list)

        for u, v in edges:
            adjList[v].append(u)
            adjList[u].append(v)

        seen = set()

        def dfs(node, prev):
            if node in seen:
                return False

            seen.add(node)
        
            for nei in adjList[node]:
                if prev != nei and not dfs(nei, node):
                    return False
            
            return True
        
        noCycle = dfs(0, -1)
        
        return noCycle and len(seen) == n
