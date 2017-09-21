# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
	def averageOfLevels(self, root):
		"""
		:type root: TreeNode
		:rtype: List[float]
		"""
		if not root:
			return []

		q = deque()
		q.append(root)
		levelAvg = []
		while q:
			ls = float(len(q))
			lsum = 0
			for i in xrange(len(q)):
				node = q.popleft()
				if node.left: q.append(node.left)
				if node.right: q.append(node.right)
				lsum += node.val

			levelAvg.append( lsum / ls )

		return levelAvg
