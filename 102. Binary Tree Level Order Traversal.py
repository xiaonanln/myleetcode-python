# Definition for a binary tree node.
# class TreeNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

class Solution(object):
	def levelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		if not root: return []

		res = []
		self.solve(root, res, 0)
		return res 

	def solve(self, root, res, lv):
		if not root: return 
		assert lv <= len(res)
		if lv == len(res):
			res.append([])

		res[lv].append(root.val)
		self.solve(root.left, res, lv+1)
		self.solve(root.right, res, lv+1)


from utils import *
t = maketree([3,9,20,None, None,15,7])
print Solution().levelOrder(t)