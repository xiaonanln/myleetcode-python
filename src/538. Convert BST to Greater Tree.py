# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def __init__(self):
		self.sum = 0

	def convertBST(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""
		def revorder(root):
			if not root: return

			revorder(root.right)
			# handle root here
			# print self.sum, root.val
			self.sum = root.val = self.sum + root.val

			revorder(root.left)

		revorder(root)
		return root 

import utils
utils.printtree(Solution().convertBST(utils.maketree([5,2,13])))