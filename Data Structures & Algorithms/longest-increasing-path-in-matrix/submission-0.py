class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if (min(i, j) < 0 or
                i >= len(matrix) or
                j >= len(matrix[0])):
                return 0

            curr = matrix[i][j]
            res = 1

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = i + dx, j + dy
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] > curr:
                    res = max(res, 1 + dfs(x, y))

            memo[(i, j)] = res

            return res

        ret = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ret = max(dfs(i, j), ret)

        return ret

