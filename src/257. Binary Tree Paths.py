# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def binaryTreePaths(self, root):
		"""
		:type root: TreeNode
		:rtype: List[str]
		"""
		if not root:
			return []
		paths = self.binaryTreePathsHelper(root)
		return ['->'.join( str(n) for n in reversed(p) ) for p in paths]

	def binaryTreePathsHelper(self, root):
		if not root.left and not root.right:
			return [[root.val]]
		elif root.left and root.right:
			LR = self.binaryTreePathsHelper(root.left)
			RR = self.binaryTreePathsHelper(root.right)
			for p in LR:
				p.append(root.val)
			for p in RR:
				p.append(root.val)

			return LR+RR
		else:
			SR = self.binaryTreePathsHelper(root.left or root.right)
			for p in SR:
				p.append(root.val)
			return SR