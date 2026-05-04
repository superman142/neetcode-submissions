class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMap = defaultdict(list)

        for u, v in prerequisites:
            adjMap[u].append(v)
        
        
        seen = set()


        def dfs(i):
            if i in seen:
                return False

            if adjMap[i] == []:
                return True

            seen.add(i)
            for pre in adjMap[i]:
                if not dfs(pre):
                    return False
            
            adjMap[i] = []
            seen.remove(i)
            
            return True
        

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True