class Solution(object):
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return 0

		S = 0
		maxS = float('-inf')
		for n in nums:
			S += n
			maxS = max(maxS, S)
			if S < 0:
				S = 0

		return maxS

print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print Solution().maxSubArray([-1])