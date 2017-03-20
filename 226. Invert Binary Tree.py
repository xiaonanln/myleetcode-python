# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return root
        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
       	return root

import useful
t = useful.maketree([1, 2, 7, 1, 3, 6, 9])
useful.printtree(t)
t = Solution().invertTree(t)
useful.printtree(t)
