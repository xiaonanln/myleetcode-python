# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def detectCycle(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		fast, slow = head, head
		while True:
			if not fast or not fast.next or not fast.next.next:
				return None

			fast = fast.next.next
			slow = slow.next

			if fast is slow:
				break

		slow = head
		while slow is not fast:
			slow = slow.next
			fast = fast.next

		return slow

import utils
print Solution().detectCycle(utils.makelist([1,2]))