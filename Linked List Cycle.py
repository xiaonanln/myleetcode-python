# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
    # @return a boolean
    def hasCycle(self, head):
        if not head: return False
        
        fast = head
        slow = head
        
        while True:
            if fast.next and fast.next.next:
                if fast.next == slow or fast.next.next == slow:
                    return True
                
                fast = fast.next.next
            else:
                return False
            
            if slow.next:
                slow = slow.next
            else:
                return False
        
            
    
