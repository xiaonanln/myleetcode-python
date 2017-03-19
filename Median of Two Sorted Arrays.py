class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        totalLen = len(A) + len(B)
        if totalLen % 2 == 1:
            return self.findkth(A, 0, len(A), B, 0, len(B), totalLen / 2)
        else:
            return (self.findkth(A, 0, len(A), B, 0, len(B), totalLen / 2) + 
                    self.findkth(A, 0, len(A), B, 0, len(B), totalLen / 2 - 1)) / 2.0
    
    def findkth(self, A, ai, aj, B, bi, bj, k):
#         print A[ai:aj], B[bi: bj], k
        Acount = aj - ai
        Bcount = bj - bi
        
        if Acount == 0:
            return B[bi + k]
        elif Bcount == 0:
            return A[ai + k]
        
        if A[aj-1] <= B[bi]:
            if k < Acount:
                return A[ai + k]
            else:
                return B[bi + k - Acount]
        
        elif B[bj-1] <= A[ai]:
            if k < Bcount:
                return B[bi + k]
            else:
                return A[ai + k - Bcount]
        
        am = (ai + aj) // 2
        bm = (bi + bj) // 2
        
        Amid, Bmid = A[am], B[bm]
        midCount = (Acount // 2 + Bcount // 2)
        
#         print k, midCount, Amid, Bmid
        
        if k < midCount:
            if Amid < Bmid:
                return self.findkth(A, ai, aj, B, bi, bm, k)
            elif Amid > Bmid:
                return self.findkth(A, ai, am, B, bi, bj, k)
            else:
                return self.findkth(A, ai, am, B, bi, bm, k)
        elif k > midCount:
            if Amid < Bmid:
                if am > ai:
                    return self.findkth(A, am, aj, B, bi, bj, k - (am-ai))
                else:
                    return B[bi + k - 1]
            elif Amid > Bmid:
                if bm > bi:
                    return self.findkth(A, ai, aj, B, bm, bj, k - (bm-bi))
                else:
                    return A[ai + k - 1]
            else:
                return self.findkth(A, am, aj, B, bm, bj, k - (am-ai) - (bm-bi))
        else: # if k == midCount
            if Amid < Bmid:
                return self.findkth(A, am, aj, B, bi, bm, k - (am-ai))
            elif Amid > Bmid:
                return self.findkth(A, ai, am, B, bm, bj, k - (bm-bi))
            else:
                return Amid
            
            
# print Solution().findMedianSortedArrays([], [])
print Solution().findMedianSortedArrays([2], [1,3,4])

















