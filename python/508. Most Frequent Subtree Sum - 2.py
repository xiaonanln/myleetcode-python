# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import Counter
class Solution(object):
	def findFrequentTreeSum(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if not root: return []
		sums = Counter()
		def postorder(root):
			ls, rs = 0, 0
			if root.left:
				ls = postorder(root.left)
			if root.right:
				rs = postorder(root.right)

			# visit root now
			s = root.val + ls + rs
			sums[s] += 1
			return s


		postorder(root)
		maxSumCount = max(sums.itervalues())
		return [s for s, c in sums.iteritems() if c == maxSumCount]

import utils
print Solution().findFrequentTreeSum(utils.maketree([5, 2, -3]))

