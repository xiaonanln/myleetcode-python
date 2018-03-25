# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def isValidBST(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		if not root:
			return True
		return self.isValidBSTHelper(root)[0]

	def isValidBSTHelper(self, root):
		if root.left:
			LV, LMin, LMax = self.isValidBSTHelper(root.left)
			if not LV: return False, None, None
			if LMax >= root.val:
				return False, None, None

			leftMin = LMin
		else:
			leftMin = root.val

		if root.right:
			RV, RMin, RMax = self.isValidBSTHelper(root.right)
			if not RV: return False, None, None
			if RMin <= root.val:
				return False, None, None
			rightMax = RMax
		else:
			rightMax = root.val

		return True, leftMin, rightMax
