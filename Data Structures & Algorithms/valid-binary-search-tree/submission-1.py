# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, -math.inf, math.inf)]

        while stack:
            node, minVal, maxVal = stack.pop()

            if not node:
                continue

            if minVal < node.val < maxVal:
                stack.append((node.left, minVal, node.val))
                stack.append((node.right, node.val, maxVal))
            else:
                return False
        
        return True
            

