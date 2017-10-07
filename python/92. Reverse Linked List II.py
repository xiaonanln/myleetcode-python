# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def reverseBetween(self, head, m, n):
		"""
		:type head: ListNode
		:type m: int
		:type n: int
		:rtype: ListNode
		"""
		prevLast = None
		post = []

		k = 0
		p = head
		revhead, revtail = None, None
		while p:
			next = p.next
			k += 1
			# print k, p.val, m,n
			if k < m:
				prevLast = p
				# print 'prevLast set to', prevLast.val
			elif k <= n:
				if not revhead:
					revhead = revtail = p
					p.next = None
				else:
					p.next = revhead
					revhead = p
			else:
				if revtail: revtail.next = p
				break

			p = next

		if prevLast and revhead: prevLast.next = revhead
		return head if prevLast else revhead

import utils
l = utils.makelist(1,2,3)
l = Solution().reverseBetween(l, 3,3)
utils.printlist(l)