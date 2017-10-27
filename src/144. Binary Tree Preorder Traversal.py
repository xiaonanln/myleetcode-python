# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def preorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		res = []
		def preorder(root):
			if not root: return
			res.append(root.val)
			preorder(root.left)
			preorder(root.right)
		preorder(root)
		return res


import utils
print Solution().preorderTraversal(utils.maketree([1, None,2,3]))