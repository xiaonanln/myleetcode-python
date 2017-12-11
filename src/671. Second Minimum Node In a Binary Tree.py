# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def findSecondMinimumValue(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		inf = float('inf')
		def smv(root):
			if not root or not root.left:
				return inf

			if root.left.val == root.val == root.right.val:
				lr = smv(root.left)
				rr = smv(root.right)
				return min(lr, rr)
			elif root.left.val == root.val:
				lr = smv(root.left)
				return min(lr, root.right.val)
			else:
				rr = smv(root.right)
				return min(rr, root.left.val)

		res = smv(root)
		return res if res != inf else -1


