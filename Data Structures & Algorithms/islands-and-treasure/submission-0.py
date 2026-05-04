class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque([])
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 2147483647

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if (min(nr, nc) < 0 or
                    nr >= ROWS or
                    nc >= COLS or
                    grid[nr][nc] != 2147483647):
                    continue
                
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))
        
