class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0]*26

        for c1, c2 in zip(s, t):
            count[ord(c1) - ord('a')] += 1
            count[ord(c2) - ord('a')] -= 1
        
        return False if any(count) else True