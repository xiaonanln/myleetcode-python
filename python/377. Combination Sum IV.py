class Solution(object):
	def combinationSum4(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		dp = [0] * (target + 1)
		dp[0] = 1
		for i in xrange(1, target+1):
			fi = 0
			for n in nums:
				if i < n: continue
				fi += dp[i - n]
			dp[i] = fi

		return dp[target]


nums = [1, 2, 3]
target = 4
print Solution().combinationSum4(nums, target)