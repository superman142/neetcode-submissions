class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        ret = 0

        seen = set()

        def dfs(i, j):
            if (min(i, j) < 0 or
                i >= ROWS or 
                j >= COLS or
                grid[i][j] == "0" or
                (i, j) in seen):
                return
            
            seen.add((i,j))
            
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

            return

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in seen:
                    dfs(i, j)
                    ret += 1
        
        return ret
            
            

            