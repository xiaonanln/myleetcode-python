# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		return self.reverseListHelper(head)[0]

	def reverseListHelper(self, head):
		if not head:
			return None, None

		reverseHead, reverseTail = self.reverseListHelper(head.next)
		if reverseHead:
			reverseTail.next = head
			head.next = None
			return reverseHead, head
		else:
			return head, head