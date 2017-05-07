# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head is None: return None
        
        nodes = []
        p = head
        while p:
            nodes.append(p)
            p = p.next
        
        nodeIndices = {}
        for i, node in enumerate(nodes):
            nodeIndices[node] = i
        
        randomIndices = [nodeIndices[n.random] if n.random else -1 for n in nodes]
        
        # start copy
        copyNodes = [RandomListNode(node.label) for node in nodes]
        for i in xrange(len(copyNodes)-1):
            copyNodes[i].next = copyNodes[i+1]
            
        for i in xrange(len(copyNodes)):
            copyNodes[i].random = copyNodes[randomIndices[i]] if randomIndices[i] != -1 else None
        
        return copyNodes[0]
        
        