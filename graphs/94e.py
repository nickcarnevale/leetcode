# https://leetcode.com/problems/binary-tree-inorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        r = []

        def dfs(root):
            if root.left:
                dfs(root.left)
            
            r.append(root.val)

            if root.right:
                dfs(root.right)

            return
        
        if root:
            dfs(root)

        return r
