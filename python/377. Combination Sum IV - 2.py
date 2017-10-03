class Solution(object):
	def combinationSum4(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		if target <= 0:
			return 0

		nums.sort()
		dp = [0] * (target+1)
		dp[0] = 1
		for t in xrange(1, target+1):
			for n in nums:
				if n > t: break
				dp[t] += dp[t-n]

		return dp[target]


print Solution().combinationSum4([1,2,3], 4)