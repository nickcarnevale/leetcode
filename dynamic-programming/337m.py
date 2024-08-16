# https://leetcode.com/problems/house-robber-iii/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # cannot rob adjacent nodes
        # cannot rob parent, and children of a particular node
        
        # dfs
        # two choices
        # rob the parent, rob both the children

        def dfs(root):

            if not root:
                return [0,0]

            leftnode = dfs(root.left)
            rightnode = dfs(root.right)

            rob1 = root.val + leftnode[1] + rightnode[1]
            rob2 = max(leftnode) + max(rightnode)

            return [rob1, rob2]

        return max(dfs(root))
       