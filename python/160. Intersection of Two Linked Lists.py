# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        LA, LB = 0, 0
        pa, pb = headA, headB
        while pa: pa = pa.next; LA += 1
        while pb: pb = pb.next; LB += 1
        pa, pb = headA, headB
        if LA > LB: 
            for _ in xrange(LA-LB): pa = pa.next
        elif LB > LA: 
            for _ in xrange(LB-LA): pb = pb.next
        while pa != pb:
            pa = pa.next
            pb = pb.next
        
        return pa