class Solution(object):
	def reorderedPowerOf2(self, N):
		"""
		:type N: int
		:rtype: bool
		"""
		nd = len(str(N))
		p2_candidates = []
		p2 = 1
		while len(str(p2)) < nd:
			p2 *= 2

		while len(str(p2)) == nd:
			p2_candidates.append(p2)
			p2 *= 2

		# print 'p2_candidates', p2_candidates
		return bool([1 for p2 in p2_candidates if sorted(str(p2)) == sorted(str(N))])


print Solution().reorderedPowerOf2(46)
