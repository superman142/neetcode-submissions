class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        stack = self.prices[:]
        ret = 0

        while stack and stack[-1] <= price:
            stack.pop()
            ret += 1
    
        self.prices.append(price)

        return ret + 1
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)