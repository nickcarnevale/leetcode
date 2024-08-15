# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        # get to the halfway point
        # reverse the second half
        # calculate twin sums
        # output max

        if head.next.next == None:
            return head.val + head.next.val


        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # slow is at halfway
        # here we need start reversing from halfway

        cur = slow
        prev = None
        nextn = None

        while cur != None:
            nextn = cur.next
            cur.next = prev
            prev = cur
            cur = nextn

        # first half is at head
        # second half is at prev
        first = head
        second = prev
        r = 0

        while second:
            r = max(r,first.val + second.val)
            first = first.next
            second = second.next

        return r



        