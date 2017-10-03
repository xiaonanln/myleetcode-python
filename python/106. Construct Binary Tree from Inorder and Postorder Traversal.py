# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from utils import TreeNode

class Solution(object):
	def buildTree(self, inorder, postorder):
		"""
		:type inorder: List[int]
		:type postorder: List[int]
		:rtype: TreeNode
		"""

		def buildTreeHelper(ii, ij, pi, pj):
			# print 'buildTreeHelper', ii, ij, pi, pj

			if ii > ij:
				return None

			# print ii, ij, pi, pj, inorder[ii:ij+1], postorder[pi:pj+1]
			rootval = postorder[pj]
			iri = inorder[ii:ij+1].index(rootval)
			root = TreeNode(rootval)
			root.left = buildTreeHelper(ii, ii+iri-1, pi, pi+iri-1)
			root.right = buildTreeHelper(ii+iri+1, ij, pi+iri, pj-1)
			return root

		return buildTreeHelper(0, len(inorder)-1, 0, len(postorder)-1)

root = Solution().buildTree([1,2,3], [1,3,2])
import utils
utils.printtree(root)