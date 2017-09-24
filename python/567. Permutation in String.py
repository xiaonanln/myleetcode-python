
from collections import Counter
class Solution(object):
	def checkInclusion(self, s1, s2):
		"""
		:type s1: str
		:type s2: str
		:rtype: bool
		"""
		if len(s2) < len(s1):
			return False

		L1 = len(s1)
		C = Counter({c: -n for c, n in Counter(s1).iteritems()})
		for c in s2[:L1]:
			C[c] += 1
			if C[c] == 0:
				del C[c]

		if not C:
			return True

		for i in xrange(L1, len(s2)):

			c = s2[i]
			C[c] += 1
			if C[c] == 0: del C[c]

			c = s2[i-L1]
			C[c] -= 1
			if C[c] == 0: del C[c]

			if not C:
				return True

		return False


s1 = "ab"; s2 = "eidbaooo"
print Solution().checkInclusion(s1, s2)

s1= "ab"; s2 = "eidboaoo"
print Solution().checkInclusion(s1, s2)