# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        memo = {}

        def dfs(node, canRob):
            if not node:
                return 0 
            
            if (node, canRob) in memo:
                return memo[(node, canRob)]

            if canRob:
                currVal = max((node.val + dfs(node.left, False) + dfs(node.right, False)), dfs(node.left, True) + dfs(node.right, True))
            else:
                currVal = dfs(node.left, True) + dfs(node.right, True)

            memo[(node, canRob)] = currVal

            return currVal
        
        return dfs(root, True)