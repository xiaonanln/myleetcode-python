"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

		 1
		/ \
	   2   5
	  / \   \
	 3   4   6

The flattened tree should look like:
   1
	\
	 2
	  \
	   3
		\
		 4
		  \
		   5
			\
			 6
"""

# Definition for a binary tree node.
# class TreeNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

class Solution(object):
	def flatten(self, root):
		"""
		:type root: TreeNode
		:rtype: void Do not return anything, modify root in-place instead.
		"""
		self.flattenHelper(root)

	def flattenHelper(self, root):
		if not root:
			return None, None

		leftHead, leftTail = self.flattenHelper(root.left)
		rightHead, rightTail = self.flattenHelper(root.right)
		if leftHead:
			root.left = None
			root.right = leftHead
			leftTail.right = rightHead
		else:
			# root.right is already set to rightHead
			pass

		tail = rightTail or leftTail or root
		return root, tail

from utils import *
t = maketree([1, 2, 5, 3, 4, None, 6])
printtree(t)

Solution().flatten(t)
printlist(t, nextKey='right')