class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = 0

        countS1 = [0]*26
        countS2 = [0]*26

        for i in range(len(s1)):
            countS2[ord(s2[i]) - ord('a')] += 1
            countS1[ord(s1[i]) - ord('a')] += 1
        
        countS2[ord(s2[len(s1) - 1]) - ord('a')] -= 1

        for r in range(len(s1) - 1, len(s2)):
            countS2[ord(s2[r]) - ord('a')] += 1

            if countS1 == countS2:
                return True

            countS2[ord(s2[l]) - ord('a')] -= 1
            l += 1
        
        return False