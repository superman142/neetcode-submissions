class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = defaultdict(int)
        preSum[0] = 1
        ret = 0

        temp = 0
        for i in range(len(nums)):
            temp += nums[i]

            if temp - k in preSum:
                ret += preSum[temp - k]
            
            preSum[temp] += 1

        return ret
        