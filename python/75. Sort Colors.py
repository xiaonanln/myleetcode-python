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

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        c0 = nums.count(0)
        c1 = nums.count(1)
        c2 = nums.count(2)
        nums[:] = [i for i, c in ((0, c0), (1, c1), (2, c2)) for _ in xrange(c)]

nums = [0]
print Solution().sortColors(nums)