class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []

        subset = []

        def dfs(i, rem):
            if rem == 0:
                ret.append(subset.copy())
                return
            
            if rem < 0:
                return 
            
            for k in range(i, len(nums)):
                subset.append(nums[k])
                dfs(k, rem - nums[k])
                subset.pop()
            
            return
        
        dfs(0, target)
        return ret

