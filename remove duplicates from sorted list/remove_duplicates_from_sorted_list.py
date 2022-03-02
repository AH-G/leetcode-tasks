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
        start=ListNode()
        if head:
            start=head
            dummy=head
            head=head.next
            while head:
                if dummy.val==head.val:
                    dummy.next=head.next
                else:
                    dummy=head
                head=head.next
            return(start)
        else:
            return(None)
