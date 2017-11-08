inf = float('inf')
class Solution(object):
	def findMin(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		return self.findMinHelper(nums, 0, len(nums))

	def findMinHelper(self, nums, l, r):
		if l >= r: return inf
		elif l == r-1: # 1 element
			return nums[l]
		elif nums[l] < nums[r-1]: # in order
			return nums[l]

		m = (l+r) // 2

		minval = min(self.findMinHelper(nums, l, m), self.findMinHelper(nums, m, r))

		return minval

print Solution().findMin([4,5,6,7,0,1,2])