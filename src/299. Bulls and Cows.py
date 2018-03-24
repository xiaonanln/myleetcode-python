from itertools import izip
from collections import Counter
class Solution(object):
	def getHint(self, secret, guess):
		"""
		:type secret: str
		:type guess: str
		:rtype: str
		"""

		A = 0
		B = 0
		C = Counter()
		for a, b in izip(secret, guess):
			if a == b:
				A += 1
				continue

			C[a] += 1
			if C[a] <= 0:
				B += 1

			C[b] -= 1
			if C[b] >= 0:
				B += 1

		return '%dA%dB' % (A, B)

print Solution().getHint('1807', '7810')