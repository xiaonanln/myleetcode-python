# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def partition(self, head, x):
		"""
		:type head: ListNode
		:type x: int
		:rtype: ListNode
		"""
		shead, stail = None, None
		gehead, getail = None, None

		node = head
		while node:
			if node.val < x:
				if shead:
					stail.next = node
					stail = node
				else:
					shead = stail = node
			else:
				if gehead:
					getail.next = node
					getail = node
				else:
					gehead = getail = node

			node = node.next

		if stail: stail.next = gehead
		if getail: getail.next = None
		return shead or gehead



# print Solution().partition()