# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
	def widthOfBinaryTree(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if not root: return 0
		q = deque()
		q.append( (1, root) )
		maxwidth = 0
		while q:
			qlen = len(q)
			minindex, maxindex = float('inf'), -float('inf')
			for _ in xrange(qlen):
				index, node = q.popleft()
				minindex = min(minindex, index)
				maxindex = max(maxindex, index)
				if node.left: q.append( (index*2, node.left) )
				if node.right: q.append( (index*2+1, node.right) )

			maxwidth = max(maxwidth, maxindex - minindex + 1)
		return maxwidth





print Solution().widthOfBinaryTree(None)