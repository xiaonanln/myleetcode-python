# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
	def bstFromPreorder(self, preorder):
		"""
		:type preorder: List[int]
		:rtype: TreeNode
		"""
		return self._constructPreorder(preorder, 0, len(preorder))

	def _constructPreorder(self, preorder, i, j):
		if i >= j:
			return None

		mid = preorder[i]
		jl = i + 1
		while jl < j and preorder[jl] < mid:
			jl += 1

		root = TreeNode(mid)
		root.left = self._constructPreorder(preorder, i + 1, jl)
		root.right = self._constructPreorder(preorder, jl, j)
		return root


print Solution().bstFromPreorder([8, 5, 1, 7, 10, 12])
