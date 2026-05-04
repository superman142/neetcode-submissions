class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in a:
                return [a[diff],i]
            a[nums[i]]=i
        #     for j in range(i+1,len(nums)):
        #         if(target-nums[i]==nums[j]):
        #             a.append(i)
        #             a.append(j)
        #             return a
        