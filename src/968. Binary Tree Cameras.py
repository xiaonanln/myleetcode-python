# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

INF = float('inf')

class Solution(object):
	def minCameraCover(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""

		if not root:
			return 0

		def solve(root):
			if not root:
				return

			solve(root.left)
			solve(root.right)

			if root.left:
				ll, lr = root.left.left, root.left.right
			else:
				ll, lr = None, None

			if root.right:
				rl, rr = root.right.left, root.right.right
			else:
				rl, rr = None, None

			l, r = root.left, root.right
			c = min(min(l._c, l._noc) if l else 0, (min(ll._c, ll._noc) if ll else 0) + (min(lr._c, lr._noc) if lr else 0)) + \
			    min(min(r._c, r._noc) if r else 0, (min(rl._c, rl._noc) if rl else 0) + (min(rr._c, rr._noc) if rr else 0)) + 1

			if not l and not r:
				noc = INF
			elif not l: # must r
				noc = r._c
			elif not r: # must l
				noc = l._c
			else: # must l and r
				noc = min(l._c + min(r._c, r._noc), r._c + min(l._c, l._noc))

			root._c, root._noc = c, noc

		solve(root)
		return min(root._c, root._noc)

import utils
null = None
root = utils.maketree([0,null,0,null,0,null,0,null,0,0,0,null,null,0,0])
print Solution().minCameraCover(root)