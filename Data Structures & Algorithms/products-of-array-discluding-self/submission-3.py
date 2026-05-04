class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*len(nums)
        right = [1]*len(nums)
        ret = [0]*len(nums)

        prod = nums[0]
        for i in range(1, len(nums)):
            left[i] = prod
            prod *= nums[i]

        prod = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            right[i] = prod
            prod *= nums[i] 

        for i in range(len(nums)):
            ret[i] = left[i]*right[i]
        
        return ret
