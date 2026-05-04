class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        buy = prices[0]

        for i in range(1, len(prices)):
            ret = max(prices[i] - buy, ret)
            buy = min(prices[i], buy)
        
        return ret

        