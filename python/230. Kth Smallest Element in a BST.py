# Definition for a binary tree node.
# class TreeNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

class Solution(object):
	def kthSmallest(self, root, k):
		"""
		:type root: TreeNode
		:type k: int
		:rtype: int
		"""
		return self.solve(root, k)[0]
		
	def solve(self, root, k):
		if not root: return None, 0
		
		n, lc = self.solve(root.left, k)
		if n is not None: 
			return n, None
		
		# kth not in left tree
		if lc == k - 1:
			return root.val, None
		# kth might be in right subtree
		n, rc = self.solve(root.right, k - lc - 1)
		if n is not None: 
			return n, None
		
		# not found ...
		return None, lc + 1 + rc
		