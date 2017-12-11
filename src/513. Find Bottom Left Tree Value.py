# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
	def findBottomLeftValue(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""

		level = [root]
		leftmost = None
		while level:
			leftmost = level[0].val
			nextlevel = []
			for node in level:
				if node.left: nextlevel.append(node.left)
				if node.right: nextlevel.append(node.right)

			level = nextlevel

		return leftmost

