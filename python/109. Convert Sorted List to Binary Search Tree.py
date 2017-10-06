# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import *

class Solution(object):
	def sortedListToBST(self, head):
		"""
		:type head: ListNode
		:rtype: TreeNode
		"""
		vals = []
		while head:
			vals.append(head.val)
			head = head.next

		def helper(i, j):
			if i >= j:
				return None

			m = (i+j) // 2
			node = TreeNode(vals[m])
			node.left = helper(i, m)
			node.right = helper(m+1, j)
			return node

		return helper(0, len(vals))