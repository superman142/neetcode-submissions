class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ret = 0

        ROWS = len(grid)
        COLS = len(grid[0])

        for i in range(ROWS):
            for j in range(COLS):
                if not grid[i][j] == 1:
                    continue
                
                if i == 0 or grid[i - 1][j] == 0:
                    ret += 1
                
                if j == 0 or grid[i][j - 1] == 0:
                    ret += 1
                
                if i == ROWS - 1 or grid[i + 1][j] == 0:
                    ret += 1
                
                if j == COLS - 1 or grid[i][j + 1] == 0:
                    ret += 1
        
        return ret
