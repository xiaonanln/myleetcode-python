class Solution(object):
	L1 = 'QWERTYUIOP'
	L2 = 'ASDFGHJKL'
	L3 = 'ZXCVBNM'

	MAP = {}
	for c in L1:
		MAP[c] = 1
		MAP[c.lower()] = 1

	for c in L2:
		MAP[c] = 2
		MAP[c.lower()] = 2

	for c in L3:
		MAP[c] = 3
		MAP[c.lower()] = 3

	def findWords(self, words):
		"""
		:type words: List[str]
		:rtype: List[str]
		"""
		return [w for w in words if self.isGood(w)]

	def isGood(self, w):
		if not w: return True
		lv = Solution.MAP[w[0]]
		for c in w:
			if Solution.MAP[c] != lv:
				return False
		return True

print Solution().findWords(["Hello", "Alaska", "Dad", "Peace"])