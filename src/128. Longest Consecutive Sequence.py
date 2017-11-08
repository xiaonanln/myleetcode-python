class Solution(object):
	def longestConsecutive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return 0

		m = {}
		for n in nums:
			if n in m: continue

			l = m.get(n-1, 0)
			r = m.get(n+1, 0)
			# print n, l, r
			if l:
				m[n-l] = l+1+r
			if r:
				m[n+r] = l+1+r

			m[n] = 1+l+r

			# print n, m

		return max(m.itervalues())



print Solution().longestConsecutive([4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3])