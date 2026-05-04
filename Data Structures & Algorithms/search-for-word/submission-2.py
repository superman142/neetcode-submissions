class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        seen = set()

        def dfs(i, j, itr):
            if itr == len(word):
                return True

            if (min(i, j) < 0 or 
                i >= ROWS or
                j >= COLS or
                (i, j) in seen or
                board[i][j] != word[itr]):
                return False
            
            seen.add((i, j))

            ret = (dfs(i + 1, j, itr + 1) or
                dfs(i, j + 1, itr + 1) or
                dfs(i - 1, j, itr + 1) or
                dfs(i, j - 1, itr + 1))
            
            seen.remove((i, j))

            return ret

        
        for i in range(ROWS):
            for j in range(COLS):
               if dfs(i, j, 0):
                return True
        
        return False
