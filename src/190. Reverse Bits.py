class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        v = 0
        for bit in xrange(0, 32):
            if (1 << bit) & n:
                v = (v << 1) + 1
            else:
                v = (v << 1)
        return v 