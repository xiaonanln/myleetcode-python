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
        
        LL, LR = self.solve(root.left)
        assert len(LL) == len(LR)
        RL, RR = self.solve(root.right)
        assert len(RL) == len(RR)
        
        for l, r in zip(LR, RL):
            l.next = r
        
        
        L = LL if len(LL) >= len(RL) else LL + RL[len(LL):]
        R = RR if len(RR) >= len(LR) else RR + LR[len(RR):]
        
        return [root] + L, [root] + R