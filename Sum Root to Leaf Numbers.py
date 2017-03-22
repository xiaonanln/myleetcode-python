# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utils import *

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if root is None: return 0
        return sum(map(int, self.solve(root)))
        
    def solve(self, root):
        if root.left is None and root.right is None:
            return [str(root.val)]
        
        L, R = [], []
        if root.left is not None:
            L = self.solve(root.left)
        if root.right is not None:
            R = self.solve(root.right)
            
        val = str(root.val)
        return [ val + s for s in L ] + [ val + s for s in R ]
        
print( Solution().sumNumbers( maketree([1,2,3]) ) )