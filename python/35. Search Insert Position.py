class Solution(object):
	def searchInsert(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		i, j = 0, len(nums)
		while i < j:
			m = (i+j) // 2
			num = nums[m]
			if num == target:
				return m
			elif target < num:
				j = m
			else:
				i = m+1

		return i


print Solution().searchInsert([1,3,5,6], 5)

assert Solution().searchInsert([1,3,5,6], 5) == 2
assert Solution().searchInsert([1,3,5,6], 2) == 1
assert Solution().searchInsert([1,3,5,6], 7) == 4
assert Solution().searchInsert([1,3,5,6], 0) == 0