class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = 1

        for i in range(len(digits) - 1, -1, -1):
            d = digits[i]
            curr = d + temp
            temp, curr = curr//10, curr % 10

            digits[i] = curr

        return [1] + digits if temp else digits