# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def countNodes(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""

		def getDepth(root):
			depth = 0
			while root:
				depth += 1
				root = root.left

			return depth

		def countNodesHelper(root):
			if not root: return 0
			ldepth = getDepth(root.left)
			rdepth = getDepth(root.right)
			if rdepth == ldepth:
				# left tree is full
				return 1 + (2 ** ldepth - 1) + countNodesHelper(root.right)
			else:
				# right tree is full
				return 1 + countNodesHelper(root.left) + (2 ** rdepth - 1)

		return countNodesHelper(root)