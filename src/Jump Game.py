class Solution1:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if A == []: return False
        
        L = [None] * len(A)
        
        return self.solve(A, 0, L)
    
    def solve(self, A, pos, L):
        if L[pos] is not None: return L[pos]
        L[pos] = self.real_solve(A, pos, L)
        return L[pos]
    
    def real_solve(self, A, pos, L):
        if pos == len(A) - 1: return True
        if pos >= len(A): return False
        if A[pos] == 0: return False
        if pos + A[pos] >= len(A)-1: return True
        
        for i in xrange(A[pos], 0, -1):
            if self.solve(A, pos+i, L):
                return True
        
        return False
    
class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if A == []: return False
        if len(A) == 1: return True
        
        d = 1
        for i in xrange(len(A)-2, 0, -1):
            if A[i] >= d:
                d = 1
            else:
                d += 1
        
        return A[0] >= d
    
    
S = Solution()
print S.canJump([2,3,1,1,4])
print S.canJump([3,2,1,0,4])
print S.canJump([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6])