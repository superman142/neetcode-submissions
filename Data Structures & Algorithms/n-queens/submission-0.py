class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        rows = set()
        cols = set()
        diag = set()
        antidiag = set()

        pos = []

        def backtrack(i, curr):
            if i == n:
                pos.append(curr[:])
                return
            
            for j in range(n):
                if (j in cols or
                    (i - j) in diag or 
                    (i + j) in antidiag):
                    continue
                
                cols.add(j)
                diag.add(i - j)
                antidiag.add(i + j)
                curr.append(j)
                backtrack(i + 1, curr)
                cols.remove(j)
                diag.remove(i - j)
                antidiag.remove(i + j)
                curr.pop()

        backtrack(0, [])

        ret = []

        def convert(res):
            ans = []

            for j in res:
                temp = ""
                for k in range(n):
                    if k == j:
                        temp += "Q"
                    else:
                        temp += "."
                ans.append(temp)
            
            return ans


        for res in pos:
            ret.append(convert(res))

        return ret

        