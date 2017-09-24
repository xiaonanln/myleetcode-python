class Solution(object):
	def sortColors(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		C = [0, 0, 0]
		for n in nums:
			C[n] += 1

		nums[:] = [n for n in (0, 1, 2) for _ in xrange(C[n])]

nums = [0]
print Solution().sortColors(nums)