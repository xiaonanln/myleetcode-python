class Solution(object):
	def wordPatternMatch(self, pattern, str):
		"""
		:type pattern: str
		:type str: str
		:rtype: bool
		"""

		P = [None] * 26
		pattern = [ord(c) - ord('a') for c in pattern]
		usedPatterns = set()
		patlen = len(pattern)
		LS = len(str)
		# print pattern
		def bt(i, si):
			# print 'bt', i, si, patlen
			if i == patlen:
				return si == LS

			p = pattern[i]
			ps = P[p]
			if ps is not None:
				if str[si:si+len(ps)] == ps:
					return bt(i+1, si + len(ps))
				else:
					return False
			else:
				for sj in xrange(si, LS):
					ps = str[si:sj+1]
					# print i, si, sj, ps, usedPatterns
					if ps in usedPatterns:
						continue

					P[p] = ps
					usedPatterns.add(ps)
					# print [P[_] for _ in pattern]
					if bt(i+1, sj+1):
						return True
					usedPatterns.discard(ps)
					P[p] = None
				return False

		return bt(0, 0)



print Solution().wordPatternMatch("abba", "dogcatcatdog")
# print Solution().wordPatternMatch('abab', 'redblueredblue')
# print Solution().wordPatternMatch('aaaa', 'asdasdasdasd')
# print Solution().wordPatternMatch('aabb', 'xyzabcxzyabc')