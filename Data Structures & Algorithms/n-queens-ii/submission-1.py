class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        diag = set()
        antiDiag = set()

        def dfs(row):
            if row == n:
                return 1
            temp = 0

            for col in range(n):
                diagVal = row - col
                antiDiagVal = row + col
                if (col in cols or
                    antiDiagVal in antiDiag or
                    diagVal in diag):
                    continue
                
                cols.add(col)
                diag.add(diagVal)
                antiDiag.add(antiDiagVal)
                temp += dfs(row + 1)
                cols.remove(col)
                diag.remove(diagVal)
                antiDiag.remove(antiDiagVal)

            return temp
        
        return dfs(0)
