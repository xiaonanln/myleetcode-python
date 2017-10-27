class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
#         print len(A)
        if not A: return 
        if len(A) == 1: return 
        
        N = len(A)
        l = 0
        r = len(A) - 1
        lw, rw = l, r
        
        while l < r:
            while l < r and A[l] == 0:
                A[lw] = 0
                lw += 1
                l += 1
 
            while l < r and A[r] == 2:
                A[rw] = 2
                rw -= 1
                r -= 1
                
            if l >= r: break 
                
            lv, rv = A[l], A[r]
            assert lv != 0 and rv != 2
            
            if rv == 0:
                A[lw] = 0
                lw += 1
            
            if lv == 2:
                A[rw] = 2
                rw -= 1
            
            l += 1
            r -= 1
            
        if l == r:
#             print l, r, A[l]
            v = A[l]
            if v == 0:
                A[lw] = 0
                lw += 1
            elif v == 2:
                A[rw] = 2
                rw -= 1
            else:
                pass
        
#         print lw, rw
        for i in xrange(lw, rw+1):
            A[i] = 1
        
        return A
            
print Solution().sortColors([])
print Solution().sortColors([0, 1, 0])
print Solution().sortColors([0, 0])
print Solution().sortColors(    [0,1,1,0,0,1,1,0,2,1,2,1,2,2,0,0,1,1,1,1,2,0,0,2,1,0,1,0,0,1,2,0,0,0,1,1,1,0,2,1,1,1,2,1,1,0,2,0,0,0,2,2,2,2,2,0,0,0,1,0,2,0,2])
# print Solution().sortColors([2,1,0])
# print Solution().sortColors([2,1,0, 0])
# print Solution().sortColors([2,1,0,1,2,0,1,2,1,2,1,2,0,0,0,1,1,2])