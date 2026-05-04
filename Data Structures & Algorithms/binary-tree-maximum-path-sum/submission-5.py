# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ret = float("-inf")

        def dfs(node):
            curr = node.val
            retVal = node.val

            if node.left:
                left = dfs(node.left)
                self.ret = max(self.ret, left)
                retVal = max(retVal, node.val + left)
                if left > 0:
                    curr += left
                    
                

            if node.right:    
                right = dfs(node.right)
                self.ret = max(self.ret, right)
                retVal = max(retVal, node.val + right)
                if right > 0:
                    curr += right
                    
            
            self.ret = max(self.ret, curr)
            self.ret = max(self.ret, retVal)

            return retVal
        
        dfs(root)

        return self.ret