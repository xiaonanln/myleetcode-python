class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printList(head):
    n = head
    vals = []
    while n is not None:
        vals.append(n.val)
        n = n.next
        
    print '->'.join(map(str, vals))
    
def makeList(values):
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
    # @return a ListNode
    def insertionSortList(self, head):
        if head is None:return None
        sorted = self.insertionSortList(head.next)
        if sorted is None: return head
        
        if head.val < sorted.val:
            head.next = sorted
            return head
        
        prev = sorted
        cur = sorted.next
        while cur is not None and cur.val < head.val:
            prev = cur
            cur = cur.next
        
        prev.next = head
        head.next = cur
        
        return sorted

root = makeList([4,19,14,5,-3,1,8,5,11,15])
Solution().insertionSortList(root)
printList(root)