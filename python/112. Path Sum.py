
class Solution(object):
	def hasPathSum(self, root, sum):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: bool
		"""
		if not root: return False
		return self.hasPathSumHelper(root, sum)

	def hasPathSumHelper(self, root, sum):
		if not root.left and not root.right:
			return root.val == sum

		else:
			has = False
			if root.left:
				has = self.hasPathSumHelper(root.left, sum - root.val)

			if not has and root.right:
				has = self.hasPathSumHelper(root.right, sum - root.val)

			return has