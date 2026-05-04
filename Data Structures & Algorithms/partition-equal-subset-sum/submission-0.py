class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False
        
        def dfs(i, rem):
            if rem == 0:
                return True

            if i == len(nums):
                return False
            
            return dfs(i + 1, rem - nums[i]) or dfs(i + 1, rem)
        
        return dfs(0, total // 2)