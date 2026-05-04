class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ret = [0]*len(temperatures)

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                _, idx = stack.pop()
                ret[idx] = i - idx
            stack.append((temperatures[i], i))

        return ret