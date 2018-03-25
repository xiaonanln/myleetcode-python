class Solution(object):
	def findMissingRanges(self, nums, lower, upper):
		"""
		:type nums: List[int]
		:type lower: int
		:type upper: int
		:rtype: List[str]
		"""
		missingRanges = []
		missingStart = lower
		for n in nums:
			if n > missingStart:
				missingRanges.append( (missingStart, n-1) )

			missingStart = n+1

		if missingStart <= upper:
			missingRanges.append((missingStart, upper))

		return ['%d->%d' % (a,b) if a<b else str(a) for a, b in missingRanges]

print Solution().findMissingRanges([0, 1, 3, 50, 75], 0, 99)

