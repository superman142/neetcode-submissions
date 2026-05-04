class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = defaultdict(int)

        for i in hand:
            count[i] += 1
        
        hand.sort()

        for i in hand:
            start = i
            if count[start] == 0:
                continue

            n = 0
            while n != groupSize and count[start + n] > 0:
                count[start + n] -= 1
                n += 1
            
            if n != groupSize:
                return False
        
        return True
