from collections import Counter
class Solution(object):
	def minWindow(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: str
		"""
		ct = Counter(t)
		cw = Counter()
		j = 0
		for c, count in ct.iteritems():
			while cw[c] < count:
				if j >= len(s):
					return ''
				cw[s[j]] += 1
				j += 1

		# print cw , j
		i = 0
		while cw[s[i]] > ct[s[i]]:
			cw[s[i]] -= 1
			i += 1

		mw = [i, j]
		# print i, j, ct, cw, mw

		while j < len(s):
			cw[s[j]] += 1
			j += 1
			while cw[s[i]] > ct[s[i]]:
				cw[s[i]] -= 1
				i += 1

			if j-i < mw[1] - mw[0]:
				mw = [i, j]

		# print 'mw', mw
		return s[mw[0]:mw[1]]


S = "ADOBECODEBANC"
T = "ABC"
print Solution().minWindow("ab","a")

