# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        return self.solve(root, False)
    
    def solve(self, root, reversed):
        if root is None:
            return []
        
        LS = self.solve(root.left, not reversed)
        RS = self.solve(root.right, not reversed)
        
        R = [ [root.val] ]
        for i in xrange( max(len(LS), len(RS)) ):
            l = LS[i] if i < len(LS) else []
            r = RS[i] if i < len(RS) else []
            rev = (not reversed) and i % 2 == 0 or (reversed and i % 2 == 1)
            R.append(l + r if not rev else r + l)
        
        return R

R = TreeNode(3)
R.left = TreeNode(9)
R.right = TreeNode(20)
R.right.left = TreeNode(15)
R.right.right = TreeNode(7)

print Solution().zigzagLevelOrder(R)