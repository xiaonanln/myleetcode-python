# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def __init__(self):
		self.res = float('-inf')

	def maxPathSum(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if not root: return 0

		def maxPathSumHelper(root):
			if not root: return float('-inf')

			lm = max(0, maxPathSumHelper(root.left))
			rm = max(0, maxPathSumHelper(root.right))

			self.res = max(self.res, root.val + lm + rm)
			return max(root.val + lm, root.val + rm)

		maxPathSumHelper(root)
		return self.res


import utils
print Solution().maxPathSum(utils.maketree([2,1,3]))