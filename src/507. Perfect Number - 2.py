from math import sqrt
class Solution(object):
	def checkPerfectNumber(self, num):
		"""
		:type num: int
		:rtype: bool
		"""
		if num <= 1: return False
		sq = int(sqrt(num))
		return sum( ((i+num/i) if i*i != num else i) for i in xrange(2, sq+1) if num % i == 0) + 1 == num

print Solution().checkPerfectNumber(1)
print Solution().checkPerfectNumber(6)
print Solution().checkPerfectNumber(28)