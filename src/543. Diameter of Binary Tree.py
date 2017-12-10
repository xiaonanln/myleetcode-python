# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def diameterOfBinaryTree(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		def helper(root):
			if not root:
				return 0, 0

			lr, ll = helper(root.left)
			rr, rl = helper(root.right)
			return max(lr, rr, ll+rl), max(ll,rl)+1

		return helper(root)[0]

import utils
t = utils.maketree([1,2,3,4,5])
print Solution().diameterOfBinaryTree(t)