class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        lo, i, hi = 0, 0, len(nums) - 1

        while i <= hi:
            if nums[i] == 0:
                swap(nums, i, lo)
                lo += 1
                i += 1
            elif nums[i] == 2:
                swap(nums, i, hi)
                hi -= 1
            else:
                i += 1
        


            