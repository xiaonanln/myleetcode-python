class Solution(object):
	def majorityElement(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		mv, mc = nums[0], 1
		for i in xrange(1, len(nums)):
			n = nums[i]
			if n == mv:
				mc += 1
			else:
				mc -= 1
				if mc < 0:
					mv, mc = n, 1
		return mv 


print Solution().majorityElement([1])
print Solution().majorityElement([1,1,2])