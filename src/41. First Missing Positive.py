class Solution(object):
	def firstMissingPositive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		CD = {}
		for n in nums:
			if n <= 0: continue
			if n in CD: continue

			l = CD.get(n-1, 0)
			r = CD.get(n+1, 0)
			CD[n-l] = CD[n+r] = CD[n] = l+1+r

		# print 'CD', CD
		return 1 + CD[1] if 1 in CD else 1

print Solution().firstMissingPositive([1,2,0])
print Solution().firstMissingPositive([3,4,-1,1])