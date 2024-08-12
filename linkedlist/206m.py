# https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head

        # store linked list in array
        # rewrite the linked list

        node = head
        store = []
        while node.next:
            store.append(node.val)
            node = node.next
        
        # catch the last val
        store.append(node.val)

        node = head
        n = len(store)
        for i in range(n-1,-1,-1):
            node.val = store[i]
            node = node.next

        return head
            

    # Solution 2 without every space complexity
    # Definition for singly-linked list.

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        curr = head
        prevn = None
        nextn = None

        while curr != None:
            nextn = curr.next
            curr.next = prevn
            prevn = curr
            curr = nextn
        
        return prevn


        


        
        