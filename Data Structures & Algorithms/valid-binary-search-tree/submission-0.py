# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isBST(root, -math.inf, math.inf)

        
    def isBST(self, root, minVal, maxVal):
        if not root:
            return True
            
        if minVal < root.val < maxVal:
            return self.isBST(root.left, minVal, root.val) and self.isBST(root.right, root.val, maxVal)
        else:
            return False
