class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        ret = []

        def dfs(curr, prev, path):
            if curr == len(s) and prev == len(s) - 1:
                ret.append(path[:])
                return
            
            if curr == len(s) and prev < len(s) - 1:
                return
            
            if s[prev + 1: curr + 1] in words:
                path.append(s[prev + 1: curr + 1])
                dfs(curr + 1, curr, path)
                path.pop()
            
            dfs(curr + 1, prev, path)

            return
        
        dfs(0, -1, [])
        sentences = []
        for brk in ret:
            sentences.append(" ".join(brk))
        
        return sentences
