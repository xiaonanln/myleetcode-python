# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printlist(head):
    n = head
    vals = []
    while n is not None:
        vals.append(n.val)
        n = n.next
        
    print '->'.join(map(str, vals))
    
def makelist(values):
    if not values: return None
    head = None
    prev = None
    for val in values:
        node = ListNode(val)
        if head is None:
            head = node
            prev = node
        else:
            prev.next = node
            prev = node
    
    return head

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        
        if m > 1:
            revPrev = head
            revStart = head.next
            nstep = m - 2
            
            for i in xrange(nstep):
                revPrev = revStart
                revStart = revStart.next
            
            revPrev.next = self.reverseBefore(revStart, n - (m-1) )
            return head
        else:
            return self.reverseBefore(head, n)
        
    def reverseBefore(self, head, n):
        h, _, _ = self.solve(head, n)
        return h
    
    def solve(self, head, n):
        if n == 1:
            return head, head, head.next
        
        newhead, newtail, next = self.solve(head.next, n-1)
        newtail.next = head
        head.next = next
        return newhead, head, next
        
            
                
            
            
            

printlist(Solution().reverseBetween(makelist([1,2,3,4,5]), 2, 4))
