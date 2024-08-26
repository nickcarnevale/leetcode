# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        cur = head
        prev = head
        while cur:
            cur = prev.next
            if cur and prev.val == cur.val:
                prev.next = cur.next
            else:
                prev = prev.next

        return head
        