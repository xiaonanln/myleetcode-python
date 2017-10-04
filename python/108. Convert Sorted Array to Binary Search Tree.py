# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import *

class Solution(object):
	def sortedArrayToBST(self, nums):
		"""
		:type nums: List[int]
		:rtype: TreeNode
		"""

		def build(i, j):
			if i > j:
				return None

			m = (i + j) // 2
			root = TreeNode(nums[m])
			root.left = build(i, m-1)
			root.right = build(m+1, j)
			return root

		return build(0, len(nums)-1)

root = Solution().sortedArrayToBST([1,2,3,4,5,6,7])
printtree(root)