class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        
        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j

            if j == len(word2):
                return len(word1) - i
            
            if (i, j) in memo:
                return memo[(i, j)]

            replace = dfs(i + 1, j + 1)
            insert = dfs(i, j + 1)
            delete = dfs(i + 1, j)

            curr = 1 + min(replace, insert, delete)

            if word1[i] == word2[j]:
                curr = min(dfs(i + 1, j + 1), curr)

            memo[(i, j)] = curr
            
            return curr
        
        return dfs(0, 0)


