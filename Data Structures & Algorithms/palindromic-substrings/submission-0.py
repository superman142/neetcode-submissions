class Solution:
    def countSubstrings(self, s: str) -> int:
        ret = 0

        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ret += 1
                l -= 1
                r += 1
            
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ret += 1
                l -= 1
                r += 1
        
        return ret