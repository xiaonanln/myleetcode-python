# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
    
printlist(Solution().mergeTwoLists(makelist([1,2,3]), makelist([1,2,3])))