'''class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        y=[]
        for i in range(len(prices)):
            x= max(prices[i+1:])
            a=x - prices[i] 
            y.append(a)
        if max(y)>0:
            return max(y)
        else:
            return 0'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res
