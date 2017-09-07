# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def pathSum(self, root, sum):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: int
		"""
		return self.pathSumHelper(root, sum, False)

	def pathSumHelper(self, root, sum, pathStarted):
		if not root:
			return 0

		n = 0
		if root.val == sum:
			# print root.val, sum
			n += 1

		if root.left:
			n += self.pathSumHelper(root.left, sum - root.val, True)
			if not pathStarted:
				n += self.pathSumHelper(root.left, sum, False)
		if root.right:
			n += self.pathSumHelper(root.right, sum - root.val, True)
			if not pathStarted:
				n += self.pathSumHelper(root.right, sum, False)

		return n


import utils
t = utils.maketree([10,5,-3,3,2,None,11,3,-2,None,1])
print Solution().pathSum(t, 8)
