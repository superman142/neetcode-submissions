class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ret = 0

        ROWS = len(grid)
        COLS = len(grid[0])

        seen = set()

        def dfs(r, c):
            if (min(r, c) < 0 or
                r >= ROWS or
                c >= COLS or
                grid[r][c] == 0 or 
                (r, c) in seen):
                return 0

            seen.add((r, c))

            return (1 + dfs(r + 1, c) +
                dfs(r - 1, c) +
                dfs(r, c + 1) +
                dfs(r, c - 1))

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in seen:
                    ret = max(ret, dfs(i, j))
        
        return ret
