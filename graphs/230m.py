# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        # stack
        arr = []
        counter = 0
        cur = root

        while cur or arr:

            # go as far left as you can
            while cur:
                arr.append(cur)
                cur = cur.left
            
            cur = arr.pop()
            counter += 1
            if counter == k:
                return cur.val
            
            cur = cur.right
            
        return -1
            

       




        