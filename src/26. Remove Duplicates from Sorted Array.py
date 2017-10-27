class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		lv = None
		w = 0
		for i, n in enumerate(nums):
			if n != lv:
				nums[w] = n
				w += 1

			lv = n

		# print nums[:w]
		return w

Solution().removeDuplicates([])
Solution().removeDuplicates([1,1,2])

Solution().removeDuplicates([1,1,2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9, 9])