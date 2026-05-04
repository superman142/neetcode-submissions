class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ret = 0
        l, r = 0, len(heights) - 1

        while l < r:
            currContain = (r - l) * min(heights[r], heights[l])
            ret = max(currContain, ret)

            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
            
        return ret