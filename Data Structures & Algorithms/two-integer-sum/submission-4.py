class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        y=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    y.append(i)
                    y.append(j)
                    return y