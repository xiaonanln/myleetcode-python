class Solution(object):
	def totalHammingDistance(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		NN = len(nums)
		res = 0
		for i in xrange(32):
			num1 = 0
			for i, n in enumerate(nums):
				num1 += (n & 1)
				nums[i] = n >> 1

			num0 = NN - num1
			res += num1 * num0

		return res

print Solution().totalHammingDistance([4, 14])
print Solution().totalHammingDistance([4, 14, 2])