class Solution(object):
	def maxProduct(self, words):
		"""
		:type words: List[str]
		:rtype: int
		"""

		N = len(words)
		WD = [0] * N
		LEN = [0] * N
		for i, w in enumerate(words):
			d = 0
			for c in w:
				c = ord(c) - 97
				d |= (1 << c)
			WD[i] = d
			LEN[i] = len(w)

		return max([LEN[i] * LEN[j] for i, d1 in enumerate(WD) for j in xrange(i+1, len(WD)) if d1 & WD[j] == 0] or 0)
