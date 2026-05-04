class Solution:
    def trap(self, heights: List[int]) -> int:
        leftMax = [0]*len(heights)
        rightMax = [0]*len(heights)

        for i in range(1, len(heights)):
            leftMax[i] = max(leftMax[i - 1], heights[i - 1])
        
        for i in range(len(heights) - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], heights[i + 1])
        ret = 0
        for i in range(len(heights)):
            minBound = min(leftMax[i], rightMax[i])
            ret += max(0, minBound - heights[i])
        
        return ret