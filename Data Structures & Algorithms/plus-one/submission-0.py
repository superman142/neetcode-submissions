class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = 1
        ret = []

        for d in digits[::-1]:
            curr = d + temp
            temp, curr = curr//10, curr % 10

            ret.append(curr)

        if temp:
            ret.append(temp)
        
        return ret[::-1]