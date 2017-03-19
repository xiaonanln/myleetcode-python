# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import useful as u

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        if root is None: return 0
        return self.solve(root)[0]
        
    def solve(self, root):
        if root.left is None and root.right is None:
            return root.val, root.val 
        
        if root.right is None:
            LS = self.solve(root.left)
            maxsum = max(LS[0], LS[1] + root.val, root.val)
            tothis = max(root.val + LS[1], root.val)
        elif root.left is None:
            RS = self.solve(root.right)
            maxsum = max(RS[0], RS[1] + root.val, root.val)
            tothis = max(root.val + RS[1], root.val)
        else:
            LS = self.solve(root.left)
            RS = self.solve(root.right)
            maxsum = max(LS[0], RS[0], LS[1] + RS[1] + root.val, LS[1] + root.val, RS[1] + root.val, root.val)
            tothis = max(root.val + max(LS[1], RS[1]), root.val)
            
#         print maxsum, tothis
        return maxsum, tothis

print Solution().maxPathSum( u.maketree([2, -1]) )