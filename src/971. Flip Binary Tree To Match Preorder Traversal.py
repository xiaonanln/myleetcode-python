# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def flipMatchVoyage(self, root, voyage):
		"""
		:type root: TreeNode
		:type voyage: List[int]
		:rtype: List[int]
		"""
		ret = []
		ok, i = self.solve(root, voyage, 0, ret)
		if not ok or i != len(voyage):
			return [-1]
		else:
			return ret

	def solve(self, root, voyage, i, ret):
		if not root:
			return True, i

		if i >= len(voyage) or root.val != voyage[i]:
			return False, i

		if not root.left and not root.right:
			return True, i + 1

		elif not root.right:  # root.left != None
			return self.solve(root.left, voyage, i + 1, ret)
		elif not root.left:  # root.right != None
			return self.solve(root.right, voyage, i + 1, ret)
		else:  # left != None && right != None
			i += 1
			if i >= len(voyage):
				return False, i

			lv = root.left.val
			if lv == voyage[i]:
				lok, i = self.solve(root.left, voyage, i, ret)
				if not lok:
					return False, i
				else:
					return self.solve(root.right, voyage, i, ret)
			else:
				ret.append(root.val)
				rok, i = self.solve(root.right, voyage, i, ret)
				if not rok:
					ret.pop()
					return False, i
				else:
					lok, i = self.solve(root.left, voyage, i, ret)
					if not lok:
						ret.pop()
					return lok, i

