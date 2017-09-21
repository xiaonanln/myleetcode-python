# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def removeElements(self, head, val):
		"""
		:type head: ListNode
		:type val: int
		:rtype: ListNode
		"""
		if not head: return head
		newhead, newtail = None, None
		p = head
		while p:
			if p.val == val:
				pass
			else:
				if not newhead:
					newhead = newtail = p
				else:
					newtail.next = p
					newtail = p

			p = p.next

		if newtail:
			newtail.next = None

		return newhead

import utils
print Solution().removeElements(utils.makelist(*[1,2,6,3,4,5,6]), 6)