class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]

        seen = set()

        while heap:
            t, i, j = heapq.heappop(heap)

            seen.add((i, j))

            if (i, j) == (n - 1, n - 1):
                return t
            
            for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                x, y = i + dx, j + dy

                if (min(x, y) < 0 or
                    x >= n or
                    y >= n or
                    (x, y) in seen):
                    continue
                heapq.heappush(heap, (max(t, grid[x][y]), x, y))

        return -1
            




