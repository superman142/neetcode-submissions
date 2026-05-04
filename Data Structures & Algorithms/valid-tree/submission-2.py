class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adjMap = defaultdict(list)

        for u, v in edges:
            adjMap[u].append(v)
            adjMap[v].append(u)

        seen = set()

        q = deque([(0, -1)])

        while q:
            curr, prev = q.popleft()

            if curr in seen:
                return False
            
            seen.add(curr)
            for neigh in adjMap[curr]:
                if neigh == prev:
                    continue
                
                if neigh in seen:
                    return False
                
                q.append((neigh, curr))
        
        return len(seen) == n

            
