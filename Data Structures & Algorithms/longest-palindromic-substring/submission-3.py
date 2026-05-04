class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo = set()
        ret = [0, 0]


        for i in range(len(s)):
            memo.add((i, i))
        
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                memo.add((i, i + 1))
                ret = [i, i + 1]


        for sz in range(3, len(s) + 1):
            for i in range(len(s) - sz + 1):
                r = i + sz - 1
                if s[i] == s[r] and (i + 1 , r - 1) in memo:
                    memo.add((i, r))
                    ret = [i, r]

        
        return s[ret[0]: ret[1] + 1]
            
        




        