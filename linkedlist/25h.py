# https://leetcode.com/problems/reverse-nodes-in-k-group/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        def Reverse(node, k):
            prev = None
            curr = node
            while k > 0:
                nextn = curr.next
                curr.next = prev
                prev = curr
                curr = nextn
                k -= 1
            return prev

        def Advance(node, k):
            for i in range(k):
                if not node:
                    return None
                node = node.next
            return node

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # Check if there are at least k nodes left
            kth = Advance(group_prev.next, k - 1)
            if not kth:
                break

            group_next = kth.next
            # Reverse the k nodes
            prev = group_next
            curr = group_prev.next

            for _ in range(k):
                nextn = curr.next
                curr.next = prev
                prev = curr
                curr = nextn

            temp = group_prev.next
            group_prev.next = prev
            group_prev = temp

        return dummy.next
