# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if  head is None: return None
        
        nodes = []
        p = head
        while p :
            nodes.append(p)
            p = p.next
            
        if n == len(nodes):
            return nodes[1] if len(nodes) > 1 else None
        else:
            nodes[-n-1].next = nodes[-n+1] if n > 1 else None
            return head
        
        