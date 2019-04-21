

class Solution(object):
	def preorder(self, root):
		"""
		:type root: Node
		:rtype: List[int]
		"""
		if not root:
			return []

		values = []
		self.visit(root, values)
		return values

	def visit(self, root, values):
		values.append(root.val)
		for child in root.children:
			self.visit(child, values)
