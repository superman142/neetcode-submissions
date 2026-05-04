class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def dfs(i, xor_val):
            if i == len(nums):
                return xor_val

            return  dfs(i + 1, xor_val^nums[i]) + dfs(i + 1, xor_val)            
        
        return dfs(0,0)