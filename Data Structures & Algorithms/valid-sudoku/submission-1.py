class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # horizontal
        M = len(board)
        N = len(board[0])

        rows = [set() for _ in range(M)]
        cols = [set() for _ in range(N)]
        squares = [[set() for i in range(3)] for j in range(3)]

        for i in range(M):
            for j in range(N):
                if board[i][j] == ".":
                    continue
                
                if (board[i][j] in rows[i] or
                    board[i][j] in cols[j] or
                    board[i][j] in squares[i//3][j//3]):
                    return False
                else: 
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    squares[i//3][j//3].add(board[i][j])
                
        return True
