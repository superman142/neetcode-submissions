class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        seen = set()
        
        def dfs(i, j):
            if (min(i, j) < 0 or
                i >= ROWS or 
                j >= COLS or
                (i, j) in seen or
                board[i][j] != "O"):
                return
            
            board[i][j] = "G"

            for di, dj in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                dfs(i + di, j + dj)
            
            return 
        
        for i in range(COLS):
            dfs(0, i)
            dfs(ROWS - 1, i)
        
        for j in range(ROWS):
            dfs(j, 0)
            dfs(j, COLS - 1)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "G":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

        return



