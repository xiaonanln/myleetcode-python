# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        c1 = l1
        c2 = l2
        result = None
        c3 = result
        C = 0
        
        while c1 or c2 or C:
            v1 = c1.val if c1 is not None else 0
            v2 = c2.val if c2 is not None else 0
            
            v = v1 + v2 + C
            if v >= 10:
                C = 1
                v -= 10
            else:
                C = 0
                
            n = ListNode(v)
            if result is None:
                result = n
                c3 = n
            else:
                c3.next = n
                c3 = n
            
            if c1: c1 = c1.next
            if c2: c2 = c2.next
        
        return result
            
        