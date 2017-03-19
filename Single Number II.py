class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        single = 0
        for bit in xrange(0, 32):
            countbit = 0
            for n in A:
                if (n >> bit) & 1:
                     countbit += 1
            
            bitisone = countbit % 3
            if bitisone:
                single |= 1 << bit
        
        return single if single <= (2 ** 31 - 1) else -(2**31) + (single - (2 ** 31))

print Solution().singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2])
    
