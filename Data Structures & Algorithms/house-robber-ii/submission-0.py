class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i, flag):
            if i >= len(nums):
                return 0
            
            if flag and i == len(nums) - 1:
                return 0

            if (i, flag) not in memo:
                memo[(i, flag)] = max(nums[i] + dfs(i + 2, flag), dfs(i + 1, flag))

            return memo[(i, flag)]
        
        return max(nums[0] + dfs(2, True), dfs(1, False))