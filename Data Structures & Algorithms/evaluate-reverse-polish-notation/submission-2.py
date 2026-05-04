class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def calculate(num1, num2, operator):
            if operator == "+":
                return num1 + num2
            elif operator == "-":
                return num1 - num2
            elif operator == "*":
                return num1 * num2
            else:
                return int(num1 / num2)


        for c in tokens:
            if c in ("+", "-", "*", "/"):
                num2 = stack.pop()
                num1 = stack.pop()
                num = calculate(num1, num2, c)
                stack.append(num)
            else:
                stack.append(int(c))
        
        return stack[-1]