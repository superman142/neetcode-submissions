class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.ret = 0
        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            if (i, buying) in dp:
                return dp[(i, buying)]

            ret = dfs(i + 1, buying)

            if buying:
                buy = dfs(i + 1, not buying) - prices[i]

                ret = max(buy, ret)
            else:
                sell = dfs(i + 2, not buying) + prices[i]

                ret = max(sell, ret)

            dp[(i, buying)] = ret

            return ret

        
        return dfs(0, True)