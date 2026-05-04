class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        total = 0
        rotten = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque([])
        seen = set()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] != 0:
                    total += 1
                
                if grid[i][j] == 2:
                    rotten += 1
                    q.append((i, j, 0))
                    seen.add((i, j))
        
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        ret = 0
        
        while q:
            r, c, time = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if (min(nr, nc) < 0 or
                    nr >= ROWS or
                    nc >= COLS or
                    grid[nr][nc] != 1 or
                    (nr, nc) in seen):
                    continue
                
                q.append((nr, nc, time + 1))
                seen.add((nr, nc))
                rotten += 1
            
            ret = max(ret, time)
            

        return ret if rotten == total else - 1

