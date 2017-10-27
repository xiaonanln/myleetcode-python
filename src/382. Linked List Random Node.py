# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import random
class Solution(object):
	def __init__(self, head):
		"""
		@param head The linked list's head.
		Note that the head is guaranteed to be not null, so it contains at least one node.
		:type head: ListNode
		"""
		self.head = head

	def getRandom(self):
		"""
		Returns a random node's value.
		:rtype: int
		"""
		p = self.head
		n = 0
		v = None
		while p is not None:
			n += 1
			if random.random() < 1.0 / n:
				v = p.val
			p = p.next

		return v



import utils
l = utils.makelist([1,2,3,4,5])
from collections import Counter
print Counter([Solution(l).getRandom() for i in xrange(100000)])
