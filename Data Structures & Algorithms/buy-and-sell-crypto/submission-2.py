class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        ret = 0

        buy = prices[0]

        for i in range(1, len(prices)):
            ret = max(ret, prices[i] - buy)
            buy = min(buy, prices[i])
        
        return ret
        