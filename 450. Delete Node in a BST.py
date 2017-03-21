# Definition for a binary tree node.
# class TreeNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

class Solution(object):
	def deleteNode(self, root, key):
		"""
		:type root: TreeNode
		:type key: int
		:rtype: TreeNode
		"""
		if not root: return None 

		if key < root.val :
			root.left = self.deleteNode(root.left, key)
		elif key > root.val:
			root.right = self.deleteNode(root.right, key)
		else: # root.val == key, removing root ...
			if root.left is None:
				root = root.right 
			elif root.right is None:
				root = root.left 
			else: # both left and right is non-empty
				root.val = self.deleteLeftMostNode(root.right, root)
				print 'delete', root.val 
		return root 

	def deleteLeftMostNode(self, root, parent):
		node = root
		isParentLeft = False
		while node.left:
			parent = node 
			node = node.left 
			isParentLeft = True

		if isParentLeft:
			parent.left = node.right
		else:
			parent.right = node.right 
		return node.val 


from utils import printtree, maketree
printtree(Solution().deleteNode(maketree([5,3,6,2,4,None,7]), 3))