# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        self.solve(root)
        
    def solve(self, root):
        if root is None: return [], []
        if root.left is None:
            return [root], [root]
        
        LL, LR = self.solve(root.left)
        RL, RR = self.solve(root.right)
        assert(len(LR) == len(RL))
        for i in xrange(len(LR)):
            LR[i].next = RL[i]
        
        return [root] + LL, [root] + RR