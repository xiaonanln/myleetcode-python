class Solution(object):
	def findPeakElement(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		# N = len(nums)
		nums.append(float('-inf'))
		for i, n in enumerate(nums):
			if nums[i-1] < n and n > nums[i+1]:
				return i

		return

print Solution().findPeakElement([1, 2, 3, 1])