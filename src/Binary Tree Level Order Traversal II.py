# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        x = self.solve(root)
        return list(reversed(x))
        
    def solve(self, root):
        if root is None: return []
        l = self.solve(root.left)
        r = self.solve(root.right)
        
        m = [ (l[i] if i < len(l) else []) + (r[i] if i < len(r) else [])
            for i in xrange(max(len(l), len(r)))]
        return [[root.val]]  + m