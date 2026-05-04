class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'{':'}', '[':']', '(':')'}

        for c in s:
            if c in brackets:
                stack.append(c)
            elif len(stack) and c == brackets[stack[-1]]:
                stack.pop()
            else:
                return False
        
        return True if len(stack) == 0 else False
        