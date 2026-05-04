class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def count(stepNo):
            if stepNo < 0:
                return 0
            
            if stepNo == 0:
                return 1
            
            if stepNo not in memo:
                memo[stepNo] = count(stepNo - 1) + count(stepNo - 2)

            return memo[stepNo]
        
        return count(n)