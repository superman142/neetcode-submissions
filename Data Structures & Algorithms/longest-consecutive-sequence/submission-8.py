class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ret = 0

        allNums = set(nums)

        for i in range(len(nums)):
            if nums[i] - 1 in allNums:
                continue
            
            count = 1
            while nums[i] + count in allNums:
                allNums.remove(nums[i] + count)
                count += 1
            ret = max(ret, count)
        
        return ret


