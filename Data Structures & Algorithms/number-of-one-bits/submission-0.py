class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0

        while n:
            ret += n % 2
            n //= 2
        
        return ret