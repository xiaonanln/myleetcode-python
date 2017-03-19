class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        from operator import xor
        return reduce(xor, A, 0)
    
sol = Solution()
print sol.singleNumber([1, 1, 2])