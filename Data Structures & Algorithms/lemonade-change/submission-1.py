class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = defaultdict(int)

        for b in bills:
            if b == 5:
                cash[b] += 1
            if b == 10:
                if cash[5] == 0:
                    return False
                
                cash[10] += 1
                cash[5] -= 1
            elif b == 20:
                temp = b - 5
                while temp >= 10 and cash[10] > 0:
                    temp -= 10
                    cash[10] -= 1
                
                while temp >= 5 and cash[5] > 0:
                    temp -= 5
                    cash[5] -= 1
                
                if temp > 0:
                    return False
                cash[20] += 1
        
        return True


