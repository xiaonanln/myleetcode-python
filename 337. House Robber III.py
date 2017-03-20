# Definition for a binary tree node.
# class TreeNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

import useful

class Solution(object):

	def rob(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		return self.solve( root, False )

	def solve(self, root, isParentRobed):
		if not root: return 0
		if isParentRobed:
			if hasattr(root, 'v1'): return root.v1 
		else:
			if hasattr(root, 'v2'): return root.v2
		
		if isParentRobed:
			ret = self.solve(root.left, False) + self.solve(root.right, False)
			root.v1 = ret
		else:
			v1 = self.solve(root.left, False) + self.solve(root.right, False)
			v2 = root.val + self.solve(root.left, True) + self.solve(root.right, True)
			ret = max(v1, v2)
			root.v2 = ret

		return ret 


print Solution().rob(useful.maketree( [3, 2, 3, None, 3, None, 1] ))
print Solution().rob(useful.maketree( [3, 4, 5, 1, 3, None, 1] ))
# useful.printtree(useful.maketree( [3, 4, 5, 1, 3, None, 1] ))
