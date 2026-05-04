class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, 0

        countS1 = [0]*26
        countS2 = [0]*26

        for c in s1:
            countS1[ord(c) - ord('a')] += 1


        def compare(countS1, countS2):

            for i in range(len(countS1)):
                if countS1[i] != countS2[i]:
                    return False
            
            return True
        

        while r < len(s2):
            while r < len(s2) and (r - l) < len(s1):
                countS2[ord(s2[r]) - ord('a')] += 1
                r += 1
            
            if compare(countS1, countS2):
                return True

            countS2[ord(s2[l]) - ord('a')] -= 1
            l += 1

        return False
            


