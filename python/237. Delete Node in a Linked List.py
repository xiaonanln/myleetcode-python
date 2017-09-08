# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def deleteNode(self, node):
		"""
		:type node: ListNode
		:rtype: void Do not return anything, modify node in-place instead.
		"""
		self.deleteNodeHelper(node)

	def deleteNodeHelper(self, node):
		if not node.next:
			return None

		node.val = node.next.val
		node.next = self.deleteNodeHelper(node.next)
		return node


import utils
head = utils.makelist([1,2,3,4])
utils.printlist(head)
Solution().deleteNode(head)
utils.printlist(head)
