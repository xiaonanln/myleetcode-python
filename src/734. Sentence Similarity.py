from itertools import izip
class Solution(object):
	def areSentencesSimilar(self, words1, words2, pairs):
		"""
		:type words1: List[str]
		:type words2: List[str]
		:type pairs: List[List[str]]
		:rtype: bool
		"""

		L1 = len(words1)
		L2 = len(words2)
		if L1 != L2:
			return False

		similar = set((a, b) if a < b else (b, a) for a, b in pairs)

		for w1, w2 in izip(words1, words2):
			if w1 == w2:
				continue

			if w1 < w2 and (w1, w2) not in similar:
				return False
			elif w2 < w1 and (w2, w1) not in similar:
				return False

		return True

print Solution().areSentencesSimilar([], [], [])
print Solution().areSentencesSimilar('great acting skills'.split(), 'fine drama talent'.split(), [["great", "fine"], ["acting","drama"], ["skills","talent"]])