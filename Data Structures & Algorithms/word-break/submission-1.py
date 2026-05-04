class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        memo = {}
        def dfs(i):
            if i == len(s):
                return True
            
            if i in memo:
                return memo[i]

            for k in range(i, len(s)):
                if s[i:k + 1] in words and dfs(k + 1):
                    memo[i] = True
                    return True
            
            memo[i] = False
            
            return False
        
        return dfs(0)