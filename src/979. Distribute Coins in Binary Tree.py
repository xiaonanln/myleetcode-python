# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def distributeCoins(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""

		if not root:
			return 0

		def postorder(node):
			if node.left:
				postorder(node.left)
			if node.right:
				postorder(node.right)

			node._sum = (node.left._sum if node.left else 0) + node.val + (node.right._sum if node.right else 0)
			node._size = (node.left._size if node.left else 0) + 1 + (node.right._size if node.right else 0)

		postorder(root)
		return self.solve(root)

	def solve(self, root):
		ret = 0

		if root.left:
			ret += self.solve(root.left)
			lsize, lsum = root.left._size, root.left._sum
			ret += abs(lsum - lsize)

		if root.right:
			ret += self.solve(root.right)
			rsize, rsum = root.right._size, root.right._sum
			ret += abs(rsum - rsize)
		return ret

import utils
print Solution().distributeCoins(utils.maketree([3, 0, 0]))