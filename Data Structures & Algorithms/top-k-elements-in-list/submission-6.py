class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] += 1
        
        for num, c in count.items():
            freq[c].append(num)
        
        ret = []
        for i in range(len(nums), -1, -1):
            for n in freq[i]:
                if len(ret) < k:
                    ret.append(n)
        
        return ret
        


        