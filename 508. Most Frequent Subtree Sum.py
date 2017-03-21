# Definition for a binary tree node.
# class TreeNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

from collections import Counter
class Solution(object):
	def findFrequentTreeSum(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		C = Counter()
		maxcount = [0]
		self.postVisit(root, C, maxcount)
		# print C, maxcount, C.items()
		return [n for n, c in C.iteritems() if c == maxcount[0]]

	def postVisit(self, root, C, maxcount):
		if not root: return 0
		vl = self.postVisit(root.left, C, maxcount)
		vr = self.postVisit(root.right, C, maxcount)
		v = root.val + vr + vl
		C[v] += 1
		maxcount[0] = max(maxcount[0], C[v])
		return v

"""
  5
 /  \
2   -3

  5
 /  \
2   -5
"""
import useful
print Solution().findFrequentTreeSum(None)
print Solution().findFrequentTreeSum(useful.maketree([5, 2, -3]))
print Solution().findFrequentTreeSum(useful.maketree([5, 2, -5]))