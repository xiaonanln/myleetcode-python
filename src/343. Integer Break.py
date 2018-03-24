class Solution(object):
	def integerBreak(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n <= 3: return n-1
		dp = [None] * 59
		dp[1] = 1
		dp[2] = 2
		dp[3] = 3
		dp[4] = 4
		dp[5] = 6
		for i in xrange(6, n+1):
			# print i, dp[:i]
			dp[i] = max(dp[i-1], 2*dp[i-2], 3*dp[i-3], 5*dp[i-5])

		return dp[n]

print Solution().integerBreak(10)