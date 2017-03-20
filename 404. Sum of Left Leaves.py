# Definition for a binary tree node.
# class TreeNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

class Solution(object):
	def sumOfLeftLeaves(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if not root:return 0
		return self.solve(root, 0)

	def solve(self, root, dir):
		if not root:
			return 0
		
		if not root.left and not root.right:
			return root.val if dir == -1 else 0
			
		return self.solve(root.left, -1) + self.solve(root.right, 1)