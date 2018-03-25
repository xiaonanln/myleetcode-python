# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def oddEvenList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		oddHead = oddTail = None
		evenHead = evenTail = None
		isOdd = True
		while head:
			next = head.next

			if isOdd:
				if not oddHead: oddHead = oddTail = head
				else:
					oddTail.next = head
					oddTail = head
			else:
				if not evenHead: evenHead = evenTail = head
				else:
					evenTail.next = head
					evenTail = head

			head = next
			isOdd = not isOdd

		if oddTail: oddTail.next = evenHead
		if evenTail: evenTail.next = None
		return oddHead