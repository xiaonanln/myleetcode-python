class Solution(object):
	def findLengthOfLCIS(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		last = float('inf')
		maxcis, cis = 0, 0
		for n in nums:
			if n > last:
				cis += 1
			else:
				cis = 1
			maxcis = max(maxcis, cis)
			last = n
		return maxcis

print Solution().findLengthOfLCIS([1,3,5,4,8])