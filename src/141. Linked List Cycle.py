# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

	def hasCycle(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""
		if not head: return False
		if not head.next or not head.next.next:
			return False

		slow = fast = head
		slow = slow.next
		fast = fast.next.next
		while fast and fast.next and fast != slow:
			fast = fast.next.next
			slow = slow.next

		return fast == slow

