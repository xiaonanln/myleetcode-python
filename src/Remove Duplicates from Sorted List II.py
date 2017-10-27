# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from utils import *

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        C = {}
        p = head
        while p:
            C[p.val] = C.get(p.val, 0) + 1
            p = p.next
        
        dummy = ListNode(0)
        prev = dummy
        p = head
#         print C
        while p:
            
            if C[p.val] == 1:
#                 print p.val
                prev.next = p
                prev = p
            
            p = p.next
        
        prev.next = None
        
        
        return dummy.next
        
head = makelist( [1, 2, 3, 3, 4, 4, 5] )
printlist(Solution().deleteDuplicates(head))


head = makelist( [1, 1, 1, 2, 3] )
printlist(Solution().deleteDuplicates(head))

