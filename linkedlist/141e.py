# https://leetcode.com/problems/linked-list-cycle/description/ 

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # hash map?

        dic = set()
        dic.add(head)

        if not head:
            return False

        while head.next:
            if head.next in dic:
                return True
            else:
                dic.add(head.next)
                head = head.next
            
        return False

        
        