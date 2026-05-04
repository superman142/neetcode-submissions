class Solution:
    def trap(self, height: List[int]) -> int:
        preMax = [0]*(len(height))
        sufMax = [0]*(len(height))

        currMax = height[0]
        for i in range(1, len(height)):
            preMax[i] = currMax
            currMax = max(currMax, height[i])
        
        currMax = height[-1]
        for i in range(len(height) - 2, -1, -1):
            sufMax[i] = currMax
            currMax = max(currMax, height[i])
        
        ret = 0

        for i in range(len(height)):
            minBound = min(preMax[i], sufMax[i])
            ret += max(0, minBound - height[i])
        
        return ret