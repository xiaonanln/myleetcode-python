def _reverseBitsHardly(n):
    rev = 0
    for i in xrange(8):
        if n & 1:
            rev = (rev << 1) + 1
        else:
            rev = rev << 1
        n = n >> 1

    return rev 

fast = {}
for i in xrange(256):
	fast[i] =  _reverseBitsHardly(i)

class Solution(object):

    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self._reverseBits32(n)

    def _reverseBits32(self, n):
    	a, b = n & 0xFFFF, n >> 16
    	a, b = self._reverseBits16(b), self._reverseBits16(a)
    	return a + (b << 16)
    
    def _reverseBits16(self, n):
    	a, b = n & 0xff, n >> 8
    	a, b = fast[b], fast[a]

    	return a + (b << 8)

print Solution().reverseBits(256)