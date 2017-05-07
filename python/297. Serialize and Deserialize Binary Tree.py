# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        seq = []
        self.genBuildSeq(root, seq)
        return ' '.join(str(e) for e in seq)

    def genBuildSeq(self, root, seq):
        if root is None:
            seq.append('N')
            return 

        self.genBuildSeq(root.left, seq)
        self.genBuildSeq(root.right, seq)
        seq.append(root.val)
        seq.append('B')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        seq = data.split()
        for i, n in enumerate(seq):
            if n not in 'BN':
                seq[i] = int(n)
        print 'seq', seq
        stack = deque()
        for s in seq:
            if s == 'N':
                stack.append(None)
            elif s == 'B':
                root = stack.pop()
                right = stack.pop()
                left = stack.pop()
                root.left = left
                root.right = right 
                stack.append(root)
            else:
                stack.append(TreeNode(s))
        assert len(stack) == 1   
        return stack.pop()
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

from utils import *
codec = Codec()
root = maketree([1, 2, 3, None, None, 4, 5])
# root = maketree([])
printtree(root)
s = codec.serialize(root)
print s
root2 = codec.deserialize(s)
printtree(root2)
