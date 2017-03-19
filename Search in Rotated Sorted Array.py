class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        D = -1
        l, r = 0, len(A) - 1
        while True:
            if A[l] <= A[r]:
                D = l
                break 
            
            elif l == r - 1:
                D = r
                break
            
            m = (l + r) / 2
#             print l, r, m
            assert m != l and m != r
            if A[l] > A[m]:
                r = m
            elif A[m] > A[r]:
                l = m
            else:
                assert False
        
        return self.solve(A, D, len(A), 0, len(A)-1, target)
    
    def solve(self, A, D, L, l, r, target):
#         print A, D, l,  r, (D+l) % L, (D+r) % L
        if l > r: return -1
        m = (l + r) / 2
        v = A[(D + m) % L]
#         print 'check', v
        if v == target:
            return (D + m) % L
        elif v > target:
            return self.solve(A, D, L, l, m-1, target)
        else:
            return self.solve(A, D, L, m+1, r, target)
        
S = Solution()
print S.search([4, 5, 6, 7, 1, 2], 1)
print S.search([4, 5, 6, 7, 1, 2], 44)
print S.search([1], 0)