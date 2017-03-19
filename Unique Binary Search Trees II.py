# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.memo = {}
    
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
            
        dp = [ [None] * (n+1) for i in xrange(n+1) ]  # dp[i][j] = [ all trees of i ~ j, i:1~n, j:1~n ]
        for i in xrange(1, n+1):
            dp[i][i] = TreeNode(i)
        
        for l in xrange(1, n+1):
            for i in xrange(1, n-l+1+1):
                j = i+l-1
                L = dp[i][j] = []
                for k in xrange(i, j+1):
                    LS = dp[i][k-1] if k > i else [None]
                    RS = dp[k+1][j] if k < j else [None]
                
                    for lt in LS:
                        for rt in RS:
                            L.append(self.newTree(k, lt, rt))
                
        return dp[1][n]
        
    def newTree(self, n, lt, rt):
        t = TreeNode(n)
        t.left = lt
        t.right = rt
        return t 
        