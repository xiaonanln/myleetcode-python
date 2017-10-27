# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if root is None: return []
        
        return self.solve(root, sum)

    def solve(self, root, sum):
        if root.left is None and root.right is None:
            return [[root.val]] if root.val == sum else []
        
        LS, RS = [], []
        if root.left :
            LS = self.solve(root.left, sum - root.val)
        
        if root.right :
            RS = self.solve(root.right, sum - root.val)
        
        return [ [root.val] + path for path in LS] + [ [root.val] + path for path in RS ]
        
    