class Solution(object):
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		N = len(nums)
		nums = [(n, i) for i, n in enumerate(nums)]
		nums.sort()
		i, j = 0, N-1

		while i < j:
			s = nums[i][0] + nums[j][0]
			if s == target:
				return [nums[i][1], nums[j][1]]
			elif s < target:
				i += 1
			else:
				j -= 1


# assert [0, 1] == [0, 1]
# assert Solution().twoSum([2,7,11,15], 9) == [0, 1]
assert Solution().twoSum([3,2,4], 6) == [1,2]