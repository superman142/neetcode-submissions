class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def dfs(rem):
            if rem < 0:
                return 0
            
            if rem == 0:
                return 1
            
            if rem in memo:
                return memo[rem]

            ret = 0
            for n in nums:
                ret += dfs(rem - n)
            
            memo[rem] = ret
            
            return ret
        
        return dfs(target)
