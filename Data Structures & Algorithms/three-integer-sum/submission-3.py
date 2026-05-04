class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ret = []

        for i in range(len(nums)):
            if i and nums[i] == nums[i - 1]:
                continue
            
            target = -nums[i]

            seen = set()
            temp = set()
            for j in range(i + 1, len(nums)):
                if target - nums[j] in seen and (target - nums[j], nums[j]) not in temp:
                    temp.add((target - nums[j], nums[j]))
                    ret.append([nums[i], target- nums[j], nums[j]])
                
                seen.add(nums[j])
            
        return ret
