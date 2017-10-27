from collections import Counter
class Solution(object):
	def isScramble(self, s1, s2):
		"""
		:type s1: str
		:type s2: str
		:rtype: bool
		"""
		if Counter(s1) != Counter(s2): return False

		def isScramble(a, b, c, d):
			C = Counter()
			i, j = a, c
			



		return isScramble(0, len(s1)-1, 0, len(s2)-1)