class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        for start in range(len(gas)):
            rem = 0 
            n = 0
            while n != len(gas):
                idx = (start + n) % len(gas)
                rem += gas[idx]
                rem -= cost[idx]
                if rem < 0:
                    break
                n += 1
            
            if n == len(gas):
                return start
        
        return -1
