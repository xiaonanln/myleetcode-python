class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p is q:
            return p

        return self.lowestCommonAncestorHelper(root, p, q)[0]

    def lowestCommonAncestorHelper(self, root, p, q):
        if not root:
            return None, False, False

        la, lp, lq = self.lowestCommonAncestorHelper(root.left, p, q)
        if la is not None:
            return la, lp, lq

        ra, rp, rq = self.lowestCommonAncestorHelper(root.right, p, q)
        if ra is not None:
            return ra, rp, rq

        fp = lp or rp or root is p
        fq = lq or rq or root is q
        return (root if fp and fq else None), fp, fq


import utils
# utils.maketree([3,5,1,6,2,0,8,null,null,7,4])
