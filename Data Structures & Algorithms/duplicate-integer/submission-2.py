class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if(nums[i]==nums[j]):
        #             return True
        # return False
        hash_set=defaultdict(int)
        n=len(nums)
        for arr in nums:
            hash_set[arr]+=1
            if(hash_set[arr]>1):
                return True
        return False