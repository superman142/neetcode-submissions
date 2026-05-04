class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = dict()

        for c in s:
            seen[c] = seen.get(c, 0) + 1
        
        for c in t:
            seen[c] = seen.get(c, 0) - 1

        for t in seen.values():
            if not t == 0:
                return False
        
        return True
        
        