class Solution:
    def isValid(self, s: str) -> bool:
        strings={")":"(","}":"{","]":"["}
        stack=[]
        for c in s:
            if c in strings:
                if stack and strings[c]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack