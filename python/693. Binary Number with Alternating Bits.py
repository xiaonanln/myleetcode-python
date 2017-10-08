class Solution(object):
	def hasAlternatingBits(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		b = 1
		lastBitIsOne = None
		while b <= n:
			if ((n & b) != 0) == lastBitIsOne:
				return False

			lastBitIsOne = (n & b) != 0
			b <<= 1

		return True
