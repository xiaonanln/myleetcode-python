# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node

    def buildTree(self, inorder, postorder):
        return self.solve((inorder, 0, len(inorder)), (postorder, 0, len(postorder)))
    
    def solve(self, inorder, postorder):
        
#         print inorder, postorder
        assert (inorder[2] - inorder[1]) == (postorder[2] - postorder[1])
        if inorder[2] == inorder[1]: return None
        
        headval = postorder[0][ postorder[2] - 1 ]
        
#         print headval
        sep = inorder[0].index(headval, inorder[1], inorder[2]) - inorder[1]
        head = TreeNode(headval)
        head.left = self.solve( (inorder[0], inorder[1], inorder[1] + sep), (postorder[0], postorder[1], postorder[1] + sep) )
        head.right = self.solve((inorder[0], inorder[1] + sep+1, inorder[2]), 
                                (postorder[0], postorder[1] + sep, postorder[2] -1))
        return head
        
def printtree(head):
    if head is None: return 
    print head.val
    printtree(head.left)
    printtree(head.right)
        
        
        
printtree(Solution().buildTree([1,2], [2,1]))