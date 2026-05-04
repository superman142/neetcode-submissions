class Solution:
    def isValid(self, s: str) -> bool:
        closingMap = {')':'(', '}':'{', ']':'['}

        stack = []

        for  b in s:
            if b not in closingMap:
                stack.append(b)
            elif stack and closingMap[b] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return True if not stack else False
