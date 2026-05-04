class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=nums
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False