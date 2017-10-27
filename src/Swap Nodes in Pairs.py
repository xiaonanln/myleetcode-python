# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        dummy = ListNode(0)
        p = dummy
        
        while head:
            if head.next:
                p.next = head.next
                head.next = head.next.next
                p.next.next = head
                p = head
                head = head.next
                
            else:
                p.next = head
                p = head
                head = head.next
                
        return dummy.next
    
import utils as u
u.printlist(Solution().swapPairs( u.makelist() ))
u.printlist(Solution().swapPairs( u.makelist(1, 2, 3, 4) ))