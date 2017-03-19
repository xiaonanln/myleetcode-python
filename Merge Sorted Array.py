class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        t = A[:m] + B[:n]
        t.sort()
        A[:] = t

A = [1,2,9, 0, 0, 0]
B = [2,3,4]
Solution().merge(A, 3, B, 3)
print A