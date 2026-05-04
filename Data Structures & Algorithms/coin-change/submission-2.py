class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(key=lambda x: -x)
        self.ret = amount + 1

        def dfs(i, change, step):

            if change < 0 or i == len(coins) or step >= self.ret:
                return

            if change == 0:
                self.ret = min(step, self.ret)
                return
            
            dfs(i, change - coins[i], step + 1)
            dfs(i + 1, change, step)
        
        dfs(0, amount, 0)

        return self.ret if self.ret != amount + 1 else -1



