class Solution(object):
	def uniquePaths(self, m, n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		"""

		dp = [[None]*n for _ in xrange(m)]
		dp[0][0] = 1
		for c in xrange(n):
			dp[0][c] = 1
		for r in xrange(m):
			dp[r][0] = 1

		for r in xrange(1, m):
			for c in xrange(1, n):
				dp[r][c] = dp[r-1][c] + dp[r][c-1]

		return dp[m-1][n-1]

print Solution().uniquePaths(3, 7)