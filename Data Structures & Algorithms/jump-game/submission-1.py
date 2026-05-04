class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        maxPossible = 0
        for i in range(len(nums) - 1):
            if i > maxPossible:
                return False
            
            maxPossible = max(i + nums[i], maxPossible)

        return maxPossible >= len(nums) - 1