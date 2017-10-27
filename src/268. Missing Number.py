class Solution(object):
	def missingNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums: return 0

		N = len(nums)
		for num in nums:
			num = num if num >= 0 else -num-1

			if num < N:
				if nums[num] >= 0: nums[num] = -1 - nums[num]

		for i, num in enumerate(nums):
			if num >= 0:
				return i

		return N


print Solution().missingNumber([0,1,3])