# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def kthSmallest(self, root, k):
		"""
		:type root: TreeNode
		:type k: int
		:rtype: int
		"""
		def kthSmallestHelper(root, k):
			# print 'kthSmallestHelper', root, root.val if root else -1, k
			if not root:
				return None, 0
			val, leftsize = kthSmallestHelper(root.left, k)
			# print 'k', k, 'val', val
			if val is not None:
				return val, 0
			if leftsize == k-1:
				return root.val, 0
			else:
				val, rightsize = kthSmallestHelper(root.right, k - leftsize - 1)
				if val is not None: return val, 0
				else: return None, leftsize+1+rightsize

		return kthSmallestHelper(root, k)[0]

import utils
print Solution().kthSmallest(utils.maketree([2,1]), 2)