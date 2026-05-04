class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []

        def backtrack(temp, op, close):
            if len(temp) == 2*n:
                ret.append(temp[:])
                return
            
            if op < n:
                backtrack(temp + '(', op + 1, close)
            
            if op > close:
                backtrack(temp + ')', op, close + 1)
            
            return

        backtrack("", 0, 0)
        return ret
