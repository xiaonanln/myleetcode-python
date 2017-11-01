class Solution(object):
	def grayCode(self, n):
		"""
		:type n: int
		:rtype: List[int]
		"""
		if n <= 0: return [0]
		# n >= 1
		v = [0, 1]
		for i in xrange(2, n+1):
			v = [0] + [(x << 1) + 1 for x in v] + [x << 1 for x in reversed(v)][:-1]

		return v





print Solution().grayCode(0)
print Solution().grayCode(1)
print Solution().grayCode(2)