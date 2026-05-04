class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.ret = 0

        memo = {}
        
        def helper(i, prev):
            if i == len(nums):
                return 0

            if (i, prev) in memo:
                return memo[(i, prev)]

            temp = 0 
            
            if prev == -1 or nums[i] > nums[prev]:
                temp = 1 + helper(i + 1, i)
            
            temp = max(temp, helper(i + 1, prev))

            memo[(i, prev)] = temp

            return temp
        
        helper(0, -1)

        return memo[(0, -1)]

            