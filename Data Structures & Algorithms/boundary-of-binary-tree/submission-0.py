# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        self.ret = [root.val]

        node = root.left

        while node:
            if node.left:
                self.ret.append(node.val)
                node = node.left
            elif node.right:
                self.ret.append(node.val)
                node = node.right
            else:
                break
        
        def getLeaves(node):
            if not node:
                return
            
            if not node.left and not node.right:
                self.ret.append(node.val)

            getLeaves(node.left)
            getLeaves(node.right)

            return
        
        getLeaves(root.left)
        getLeaves(root.right)

        stack = []

        node = root.right

        while node:
            if node.right:
                stack.append(node.val)
                node = node.right
            elif node.left:
                stack.append(node.val)
                node = node.left
            else:
                break
    
        self.ret += stack[::-1]
        return self.ret