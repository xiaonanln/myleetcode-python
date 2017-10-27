class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 1
        if n == 1: return 10

        tm = 10
        m = 9
        n -= 1
        d = 9
        while n > 0:
        	m *= d
        	tm += m
        	n -= 1
        	d -= 1
        return tm


print Solution().countNumbersWithUniqueDigits(0) 
print Solution().countNumbersWithUniqueDigits(1) == 10
print Solution().countNumbersWithUniqueDigits(2) == 10+9*9
print Solution().countNumbersWithUniqueDigits(3) == 10+9*9+9*9*8
