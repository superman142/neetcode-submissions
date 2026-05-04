class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = {}

        for i in nums:
            visited[i] = visited.get(i,0) + 1
        
        if len(nums) == len(visited.keys()):
            return False
        
        return True