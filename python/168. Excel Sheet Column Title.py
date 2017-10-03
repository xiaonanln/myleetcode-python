class Solution(object):
	def convertToTitle(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		a = 26; b = 0; d = 1
		while n > (b+a):
			b += a
			a *= 26
			d += 1

		n = n - b - 1

		s = ''
		for dd in xrange(d, 0, -1):
			m, n = divmod(n, 26**(dd-1))
			s = s + chr(65+m)

		return s

print Solution().convertToTitle(701)