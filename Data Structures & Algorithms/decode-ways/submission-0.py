class Solution:
    def numDecodings(self, s: str) -> int:
        
        def dfs(i):
            if i >= len(s):
                return 1
            
            temp = 0

            if 1 <= int(s[i]) <= 26:
                temp += dfs(i + 1)
            
            if i <= len(s) - 2 and s[i] in ["1", "2"] and 1 <= int(s[i:i+2]) <= 26:
                temp += dfs(i + 2)
            
            return temp
        
        return dfs(0)
