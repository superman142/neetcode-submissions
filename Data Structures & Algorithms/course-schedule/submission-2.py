class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)

        for u, v in prerequisites:
            adjList[u].append(v)

        seen = set()

        def dfs(node, path):
            if node in path:
                return False
            
            path.add(node)

            if node in seen:
                return True
            
            for nei in adjList[node]:
                if not dfs(nei, path):
                    return False
            
            path.remove(node)
            seen.add(node)
            
            return True
        
        for i in range(numCourses):
            if not dfs(i, set()):
                return False
        
        return True

        