import math
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1: return False
        return sum(i + num/i if i != 1 and i != num/i else i for i in xrange(1, int(math.sqrt(num))+1) if num % i == 0) == num