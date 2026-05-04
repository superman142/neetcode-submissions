class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def count(n):
            ret = 0
            while n:
                n &= (n - 1)
                ret += 1
            
            return ret
        
        return [count(i) for i in range(n + 1)]