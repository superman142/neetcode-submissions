class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = dict()

        for i in range(len(nums)):
            if target - nums[i] in mem.keys():
                return [mem[target - nums[i]], i]
            else:
                mem[nums[i]] = i
        
        return []
        