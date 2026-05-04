class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        ret = 1
        count = defaultdict(int)

        for i in range(len(nums)):
            count[nums[i]] = 1
        
        for n in nums: 
            if n not in count:
                continue
            
            curr = n + 1
            counter = count[n]
            while curr in count:
                counter += count[curr]
                count.pop(curr)
                curr += 1

            count[n] = counter
            
            ret = max(counter, ret)
        
        return ret