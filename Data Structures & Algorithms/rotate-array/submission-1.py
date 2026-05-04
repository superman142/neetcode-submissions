class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rotate(l, h):
            while l < h:
                nums[l], nums[h] = nums[h], nums[l]
                l += 1
                h -= 1
        
        k %= len(nums)

        rotate(0, len(nums) - 1)
        rotate(0, k - 1)
        rotate(k, len(nums) - 1)
            