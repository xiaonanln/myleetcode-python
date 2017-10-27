# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root is None: return False
        
        return self.solve(root, sum)
    
    def solve(self, root, sum):
        
        if root.left  is None and root.right is None:
            return root.val == sum
        
        if root.left is None:
            return self.solve(root.right, sum - root.val)
        elif root.right is None:
            return self.solve(root.left, sum - root.val)
        else:
            return self.solve(root.right, sum - root.val) or \
                self.solve(root.left, sum - root.val)
        