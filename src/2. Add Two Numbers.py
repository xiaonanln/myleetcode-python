# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from utils import ListNode, makelist, printlist


class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		head = tail = ListNode(None)
		c = 0
		while l1 or l2 or c:
			val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + c
			node = ListNode(val % 10)
			c = val >= 10
			tail.next = node
			tail = node
			if l1: l1 = l1.next
			if l2: l2 = l2.next

		return head.next

l1 = makelist(1,2,3)
l2 = makelist(1,2,7)
printlist(Solution().addTwoNumbers(l1, l2))
