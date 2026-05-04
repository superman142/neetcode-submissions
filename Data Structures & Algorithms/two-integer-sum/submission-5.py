class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = dict()

        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in numMap.keys():
                return [numMap[rem], i]
            numMap[nums[i]] = i
        
        return []


