class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = float('-inf')
        l = 0
        h = 0

        currSum = 0
        while h < len(nums):
            currSum += nums[h]
            ret = max(ret, currSum)
            while currSum < 0:
                currSum -= nums[l]
                l += 1
            h += 1
        
        return ret
