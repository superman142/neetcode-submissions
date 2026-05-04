class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []

        seen = set()
        def backtrack(temp):
            if len(temp) == len(nums):
                ret.append(temp[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in seen:
                    temp.append(nums[i])
                    seen.add(nums[i])
                    backtrack(temp)
                    temp.pop()
                    seen.remove(nums[i])
            
            return
        
        backtrack([])

        return ret



