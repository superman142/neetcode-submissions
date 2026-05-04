class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        adjList = defaultdict(list)

        for crs, pre in prerequisites:
            adjList[pre].append(crs)
            indegree[crs] += 1

        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        ret = []

        while q:
            node = q.popleft()
            ret.append(node)

            for nei in adjList[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return ret if len(ret) == numCourses else []
