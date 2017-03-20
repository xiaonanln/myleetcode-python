
from collections import deque
class Solution(object):
	def convert(self, s, numRows):
		"""
		:type s: str
		:type numRows: int
		:rtype: str
		"""
		if numRows <= 1 or len(s) <= 1: 
			return s

		qs = [deque() for _ in xrange(numRows)]
		r = 0
		dir = 1
		for c in s:
			qs[r].append(c)

			if r == numRows - 1:
				dir = -1
			elif r == 0:
				dir = 1

			r += dir

		return ''.join((c for q in qs for c in q))


print Solution().convert("", 1)
print Solution().convert("PAYPALISHIRING", 3)