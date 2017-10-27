class Solution(object):
	def moveZeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		w = 0
		for r, n in enumerate(nums):
			if n != 0:
				nums[w] = n
				w += 1

		nums[w:] = [0] * (len(nums)-w)

l = [1,0,2,0,3,0]
Solution().moveZeroes(l)
print l