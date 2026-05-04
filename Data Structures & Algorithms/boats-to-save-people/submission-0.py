class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ret = 0

        l, h = 0, len(people) - 1

        while l <= h:
            curr = people[l] + people[h]

            if curr <= limit:
                l += 1
                h -= 1
            else:
                h -= 1
            
            ret += 1
        
        if l == h:
            ret += 1
        
        return ret 
