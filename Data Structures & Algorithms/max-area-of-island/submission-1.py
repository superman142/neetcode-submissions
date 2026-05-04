class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        seen = set()

        def dfs(i, j):
            if (min(i, j) < 0 or
                i >= ROWS or
                j >= COLS or
                grid[i][j] == 0 or
                (i, j) in seen):
                return 0
            
            seen.add((i, j))
            count = 1
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i + dx, j + dy
                count += dfs(x, y)
            
            return count

        ret = 0
        for i in range(ROWS):
            for j in range(COLS):
                ret = max(ret, dfs(i, j))
        
        return ret

