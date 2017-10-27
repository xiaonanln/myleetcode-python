# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def isBalanced(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""

		def postorder(root):
			if not root: return True, 0

			ok, ldepth = postorder(root.left)
			if not ok: return False, 0

			ok, rdepth = postorder(root.right)
			if not ok or abs(ldepth-rdepth) > 1: return False, 0
			return True, 1+max(ldepth, rdepth)

		return postorder(root)[0]

