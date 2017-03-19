# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head: return head 

        p1, p2 = None, None
        t1, t2 = None, None
        
        p = head
        while p:
            next = p.next
            if p.val < x:
                # append to p1
                if p1:
                    t1.next = p
                    t1 = p
                else:
                    p1 = t1 = p   
            else:
                # append to p2
                if p2:
                    t2.next = p
                    t2 = p
                else:
                    p2 = t2 = p
        
            p = next
        
        if not p1:
            t2.next = None
            return p2
            
        if not p2:
            t1.next = None
            return p1
            
        t1.next = p2
        t2.next = None
        return p1
                        
                
from useful import makelist,printlist
printlist(Solution().partition(makelist(1,1), 2))
