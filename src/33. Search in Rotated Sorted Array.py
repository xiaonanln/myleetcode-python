from bisect import bisect_left
class Solution(object):
	def search(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		l, r = 0, len(nums)
		while l < r:
			if nums[l] <= nums[r-1]:
				# in order, just use bisect
				bi = bisect_left(nums, target, l, r)
				return bi if bi < r and nums[bi] == target else -1

			m = (l+r) // 2
			if nums[m] == target:
				return m

			if l <= m-1:
				if nums[l] <= nums[m-1]:
					if nums[l] <= target <= nums[m-1]:
						r = m
					else:
						l = m +1
				else:
					assert nums[m+1] <= nums[r-1]
					if nums[m+1] <= target <= nums[r-1]:
						l = m+1
					else:
						r = m
			else:
				l = m+1

		return -1

print Solution().search([0, 1, 2, 4, 5, 6, 7], 4)
print Solution().search([4, 5, 6, 7,0, 1, 2], 4)