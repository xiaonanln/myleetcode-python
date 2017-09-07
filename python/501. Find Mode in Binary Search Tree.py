# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import Counter


class Solution(object):
	def findMode(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if not root:
			return []

		C = Counter()

		def travel(root):
			if root:
				C[root.val] += 1
				travel(root.left)
				travel(root.right)

		travel(root)

		maxcount = max(C.itervalues())
		return [n for n, c in C.iteritems() if c == maxcount]