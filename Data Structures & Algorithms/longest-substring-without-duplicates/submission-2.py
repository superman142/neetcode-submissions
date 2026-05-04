class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        ret = 0
        i = 0
        for j, c in enumerate(s):
            count[c] += 1
            while count[c] > 1:
                count[s[i]] -= 1
                i += 1
            
            ret = max(ret, j - i + 1)
        
        return ret