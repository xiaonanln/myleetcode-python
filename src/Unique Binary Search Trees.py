class Solution:
    # @return an integer
    def numTrees(self, n):
        R = [0] * max((n + 1), 3)
        R[0] = 1
        R[1] = 1
        R[2] = 2
        
        for i in xrange(3, n+1):
            tr = 0
            for h in xrange(0, i):
                ln = h
                rn = i - h - 1
#                 print i, ln, rn, R[ln], R[rn]
                tr += R[ln] * R[rn]
            R[i] = tr
        
        return R[n]
                
print Solution().numTrees(1)
print Solution().numTrees(2)
print Solution().numTrees(3)