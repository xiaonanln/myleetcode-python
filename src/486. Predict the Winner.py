class Solution(object):
	def PredictTheWinner(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		N = len(nums)
		dp = [ [None] * (N+1) for _ in xrange(N)]
		for i in xrange(N):
			dp[i][i] = 0
			dp[i][i+1] = nums[i]

		for l in xrange(2, N+1): # l = 2 ~ N
			for i in xrange(0, N-l+1):
				j = i + l
				dp[i][j] = max(
					nums[j-1] - dp[i][j-1],
					nums[i] - dp[i+1][j],
				)
		return dp[0][N] >= 0

print Solution().PredictTheWinner( [1, 5, 2] )
print Solution().PredictTheWinner( [1, 5, 233, 7] )