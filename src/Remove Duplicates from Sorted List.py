# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None: return None
        
        saw = set()
        saw.add(head.val)
        prev, p = head, head.next
#         print saw, p.val
        while p is not None:
            if p.val not in saw:
                saw.add(p.val)
                prev.next = p
                prev = p
                p = p.next
            
            else:
                p = p.next
            
        prev.next = None
        return head

def printList(head):
    n = head
    vals = []
    while n is not None:
        vals.append(n.val)
        n = n.next
        
    print '->'.join(map(str, vals))

a = ListNode(1)
a.next = ListNode(1)
printList(a)
printList(Solution().deleteDuplicates(a))