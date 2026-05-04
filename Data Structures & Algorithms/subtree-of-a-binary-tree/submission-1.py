# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        ret = False

        if root and subRoot and root.val == subRoot.val:
            ret = self.isSameTree(root, subRoot)
        
        if not ret:
            ret = self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        return ret
        
    

    def isSameTree(self, s, t):
        if not s and not t:
            return True
        
        if s and t and s.val == t.val:
            return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
        
        return False
    