class Solution(object):
	def findDisappearedNumbers(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		for i, n in enumerate(nums):
			if n < 0: n = -n
			if nums[n-1] > 0:
				nums[n-1] = -nums[n-1]

		return [i+1 for i, n in enumerate(nums) if n > 0]

print Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1])