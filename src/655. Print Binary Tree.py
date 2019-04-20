# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def printTree(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[str]]
		"""
		def depth(root):
			if not root:
				return 0

			return 1 + max(depth(root.left), depth(root.right))

		D = depth(root)
		W = [0] * (D+1)
		for i in xrange(1, D+1):
			W[i] = W[i-1] * 2 + 1

		ret = [
			[""] * W[D] for _ in xrange(D)
		]

		def solve(root, d, r, c):
			if not root:
				return

			ret[r][c] = str(root.val)
			solve(root.left, d-1, r + 1, c - W[d-1] + W[d-1]//2)
			solve(root.right, d-1, r + 1, c + W[d-1] // 2 + 1)

		solve(root, D, 0, W[D]//2)

		return ret

