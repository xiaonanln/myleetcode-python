# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def postorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if not root: return []

		stack = []
		stack.append((1, root))
		postorder = []
		while stack:
			op, root = stack.pop()
			if op == 1:
				stack.append((2, root))
				if root.right:
					stack.append((1, root.right))
				if root.left:
					stack.append((1, root.left))
			else:
				postorder.append(root.val)
		return postorder

import utils
print Solution().postorderTraversal(utils.maketree([1,None,2,3]))

