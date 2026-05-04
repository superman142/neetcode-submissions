"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        R = len(grid)
        C = len(grid[0])

        def dfs(rs, re, cs, ce):

            gridVal = grid[rs][cs]
            breakGrid = False

            for i in range(rs, re + 1):
                if breakGrid:
                    break
                for j in range(cs, ce + 1):
                    if grid[i][j] != gridVal:
                        breakGrid = True
                        break
            
            curr = Node(gridVal, True, None, None, None, None)
            
            if breakGrid:
                curr.isLeaf = False
                rBreak = (rs + re) // 2
                cBreak = (cs + ce) // 2
                curr.topLeft = dfs(rs, rBreak, cs, cBreak)
                curr.topRight = dfs(rs, rBreak, cBreak + 1, ce)
                curr.bottomLeft = dfs(rBreak + 1, re, cs, cBreak)
                curr.bottomRight = dfs(rBreak + 1, re, cBreak + 1, ce)

            return curr

        return dfs(0, R - 1, 0, C - 1)
        

        



              