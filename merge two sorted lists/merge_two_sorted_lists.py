# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        finallist=ListNode()
        dummy=finallist
        while (l1) and (l2):
            if l1.val<=l2.val:
                dummy1=ListNode(l1.val)
                dummy.next=dummy1
                dummy=dummy.next
                l1=l1.next
            else:
                dummy1=ListNode(l2.val)
                dummy.next=dummy1
                dummy=dummy.next
                l2=l2.next
        if (not l1) and l2:
            dummy.next=l2
        elif (not l2) and l1:
            dummy.next=l1
        finallist=finallist.next
        return finallist
