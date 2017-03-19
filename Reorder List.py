# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head: return None
        if not head.next: return head
        
        
        p = head
        nodes = []
        while p:
            nodes.append(p)
            p = p.next
        
        rl = nodes[0]
        rl.next = nodes[-1]
        tail = rl.next
        tail.next = None
        for i in xrange(1, len(nodes) // 2):
            n = nodes[i]
            tail.next = n
            tail = tail.next
            tail.next = nodes[len(nodes) - 1 - i]
            tail = tail.next
         
        if len(nodes) % 2 == 1:
            n = nodes[len(nodes) // 2]
            tail.next = n
            tail = tail.next
             
        tail.next = None
            
        return head

def printList(l):
    while l is not None:
        print l.val, 
        l = l.next
    print 
    
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)

printList(a)
printList(Solution().reorderList(a))