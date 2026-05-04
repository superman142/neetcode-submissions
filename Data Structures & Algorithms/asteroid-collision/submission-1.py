class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for val in asteroids:
            while stack and stack[-1] > 0 and val < 0:
                if abs(stack[-1]) > abs(val):
                    val = 0
                    break
                elif abs(stack[-1]) == abs(val):
                    val = 0
                
                stack.pop()
            
            if val != 0:
                stack.append(val)
        
        return stack
        


