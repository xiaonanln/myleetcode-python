# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root is None: return True
        
        return self.solve(root.left, root.right)

    def solve(self, left, right):
        if left is None and right is None:
            return True
        
        if left is None or right is None: 
            return False
        
        if left.val != right.val:
            return False
        
        return self.solve(left.left, right.right) and self.solve(left.right, right.left)

import utils as u
print Solution().isSymmetric( u.maketree( [1, 2, 2, 3, 4, 4, 3] ) )
print Solution().isSymmetric( u.maketree( [1, 2, 2, None, 3, None, 3] ) )