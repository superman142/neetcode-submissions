class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ret = 0
        numSet = set(nums)

        for n in nums:
            if n - 1 not in numSet:
                temp = n
                count = 0
                while temp in numSet:
                    count += 1
                    temp += 1

                ret = max(ret, count)

        return ret
        
