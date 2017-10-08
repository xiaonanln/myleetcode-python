# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
	def copyRandomList(self, head):
		"""
		:type head: RandomListNode
		:rtype: RandomListNode
		"""
		if not head: return None

		p = head
		copyNodes = []
		while p:
			cp = RandomListNode(p.label)
			copyNodes.append(cp)
			cp.next = p
			next = p.next
			p.next = cp
			p = next 

		# copy random now
		for cp in copyNodes:
			r = cp.next.random
			cp.random = r.next if r else None

		for i, cp in enumerate(copyNodes):
			cp.next.next = copyNodes[i+1].next if i < len(copyNodes)-1 else None
			cp.next = copyNodes[i+1] if i < len(copyNodes)-1 else None

		return copyNodes[0]

