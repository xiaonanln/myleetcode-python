class Solution(object):
	def arrayPairSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		nums.sort()
		return sum(nums[i] for i in xrange(0, len(nums), 2))

