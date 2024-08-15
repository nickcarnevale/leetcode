# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # similar to twin sums
        # first get to halfway
        # if odd ignore middle

        even = False

        slow = head
        fast = head

        # this moves fast to the end and slow to the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == None:
                even = True

        def reverse(node):

            currNode = node
            prevNode = None
            nextNode = None

            while currNode:
                nextNode = currNode.next
                currNode.next = prevNode
                prevNode = currNode
                currNode = nextNode

            # return reversed head
            return prevNode


        # slow now holds the middle
        # if n is even
        # reverse from slow
        # if n is odd
        # reverse from one after slow
        
        first = head
        second = None
        
        if even:
            second = reverse(slow)
        else:
            second = reverse(slow.next)

        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True 



        
        