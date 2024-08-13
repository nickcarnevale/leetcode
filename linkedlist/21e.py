# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        r = ListNode()
        cur = r

        while list1 != None and list2 != None: 
            
            if list1.val <= list2.val:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
            else:
                cur.next = list2
                cur = cur.next
                list2 = list2.next

        # catch strays
        if list1 != None:
            cur.next = list1
        else:
            cur.next = list2

        return r.next
        