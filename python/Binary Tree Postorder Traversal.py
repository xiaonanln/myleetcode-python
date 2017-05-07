# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if root is None: return []
        
        stack = collections.deque()
        
        stack.append( (True, root) )
        result = []
        
        while stack:
            rec, node = stack.pop()
            if not rec:
                result.append(node.val)
            else:
                stack.append( ( False, node) )
                if node.right: stack.append( (True, node.right) )
                if node.left: stack.append( (True, node.left) )
                
        
        return result
    
print Solution().postorderTraversal(TreeNode(3))