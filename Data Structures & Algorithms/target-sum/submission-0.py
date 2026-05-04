class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, curr):
            if i == len(nums) and curr == target:
                return 1
            
            if i == len(nums):
                return 0

            if (i, curr) in memo:
                return memo[(i, curr)]

            ret = 0
            ret = dfs(i + 1, curr - nums[i]) + dfs(i + 1, curr + nums[i])
            memo[(i, curr)] = ret

            return ret
        
        return dfs(0, 0)