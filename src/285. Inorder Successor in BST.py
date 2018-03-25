# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def inorderSuccessor(self, root, p):
		"""
		:type root: TreeNode
		:type p: TreeNode
		:rtype: TreeNode
		"""

		if p.right:
			pr = p.right
			while pr.left:
				pr = pr.left

			return pr

		# p has no right, find p's parent
		succ = None
		while root:
			if p.val < root.val:
				succ = root
				root = root.left

			elif p.val > root.val:
				root = root.right
			else: # p is root, no parent
				break

		return succ

from utils import *
t = maketree([3,1,4,None,2])
print Solution().inorderSuccessor(t, t.left.right)