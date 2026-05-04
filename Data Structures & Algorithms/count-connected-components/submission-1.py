class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ret = 0
        
        adjMap = defaultdict(list)

        for u, v in edges:
            adjMap[u].append(v)
            adjMap[v].append(u)
        
        seen = set()

        def bfs(i):
            q = deque([i])

            while q:
                node = q.popleft()
                seen.add(node)

                for nei in adjMap[node]:
                    if nei not in seen:
                        q.append(nei)
            
            return

        for i in range(n):
            if i not in seen:
                bfs(i)
                ret += 1

        return ret