class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        a=1
        y=[]
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==0:
                a+=0
            elif nums[i+1]-nums[i]==1:
                a+=1
            else:
                y.append(a)
                a=1
        y.append(a)
        return max(y)