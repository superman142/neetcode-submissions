class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        hi = max(piles)

        def canEat(k):
            hours = 0

            for p in piles:
                hours += p // k
                hours += 1 if p % k else 0
            
            return True if hours <= h else False

        while l < hi:
            mid = (l + hi) // 2

            if canEat(mid):
                hi = mid
            else:
                l = mid + 1
        
        return l