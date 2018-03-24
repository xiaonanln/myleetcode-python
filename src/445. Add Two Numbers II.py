# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		n1 = self.ll2num(l1)
		n2 = self.ll2num(l2)
		n3 = n1 + n2
		return self.num2ll(n3)

	def ll2num(self, head):
		n = head.val
		while head.next:
			head = head.next
			n = n * 10 + head.val

		return n

	def num2ll(self, n):
		print 'num2ll', n
		head = ListNode(n % 10)
		n //= 10

		while n:
			newhead = ListNode(n % 10)
			n //= 10
			newhead.next = head
			head = newhead

		return head
