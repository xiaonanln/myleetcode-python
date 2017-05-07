import sys

class Solution(object):

	chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	def convertToTitle(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		if n <= 26:
			return Solution.chars[n-1]

		d = 26
		t = 26
		while t + d * 26 < n:
			d *= 26
			t += d

		s = ''
		while d > 0:
			# print >>sys.stderr, s, d, n, t, Solution.chars[(n - t) // d]
			if d == 1:
				s += Solution.chars[(n - t) // d -1]
			else:

				s += Solution.chars[(n - t-1) // d]

			n = (n - t) % d + (t-d)
			t -= d
			d //= 26
			# print >>sys.stderr, 'new', n, t, d

		return s

# print Solution().convertToTitle(27)

def check(n, s):
	ss = Solution().convertToTitle(n)
	assert ss == s, (n, ss, s)

check(27, 'AA')
check(28, 'AB')
check(52, 'AZ')
