class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        i = 0
        ret = 1

        seen = set()
        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])

            ret = max(ret, j - i + 1)
        
        return ret

