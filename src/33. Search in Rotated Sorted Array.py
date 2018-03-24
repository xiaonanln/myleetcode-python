
from bisect import bisect_left
class Solution(object):
	def search(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		i, j = 0, len(nums)

		while i < j:
			if nums[i] <= nums[j-1]:
				k = bisect_left(nums, target, i, j )
				return k if k != j and nums[k] == target else -1

			if j-i < 3:
				try: return nums[i:j].index(target) + i
				except ValueError: return -1

			m = (i+j) // 2
			if nums[m] == target:
				return m

			if nums[i] <= nums[m-1]:
				# left is in order
				if nums[i] <= target <= nums[m-1]:
					j = m
				else:
					i = m+1
			else:
				# right is in order
				if nums[m+1] <= target <= nums[j-1]:
					i = m+1
				else:
					j = m

		return -1

print Solution().search([1], 0)