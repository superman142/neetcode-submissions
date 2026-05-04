class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        possible = [0]*3

        for a, b, c in triplets:
            t1, t2, t3 = target

            if a > t1 or b > t2 or c > t3:
                continue
            
            if a == t1:
                possible[0] = 1
            
            if b == t2:
                possible[1] = 1
            
            if c == t3:
                possible[2] = 1
            
        return sum(possible) == 3
        