class Solution(object):
	def wiggleSort(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		nums.sort()
		i = (len(nums)+1) // 2 - 1
		j = len(nums) - 1
		if j % 2 == 1: j -= 1
		# print 'start', i, j
		while i >= 0:
			nums[i], nums[j] = nums[j], nums[i]
			i -= 1
			j -= 2
			# print i, j

nums = [1,2,3]
Solution().wiggleSort(nums)
print nums