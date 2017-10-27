class Solution(object):
	def totalHammingDistance(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		ones = [0] * 32
		total = 0
		for i, num in enumerate(nums):
			for b in xrange(32):
				if num & (1<<b):
					total += (i - ones[b])
				else:
					total += ones[b]

				if num & (1<<b):
					ones[b] += 1

		return total


print Solution().totalHammingDistance([4, 14, 2 ])

