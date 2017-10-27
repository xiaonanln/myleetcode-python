# ! Amazing! After studying Algorithms for many weeks, now I can solve these hard questions
# which I never had a clear thinking process. And also I can write clean DP code now.

M = 10**9 + 7
class Solution(object):
	def kInversePairs(self, N, K):
		"""
		:type N: int
		:type K: int
		:rtype: int
		"""

		# dp formula dp[n,k] = dp[n,k-1] - dp[n-1,k-1-(n-1)] + dp[n-1,k]
		dp = [[0] * (K + 1) for _ in xrange(N + 1)]
		for n in xrange(0, N+1):
			dp[n][0] = 1
		for k in xrange(0, K+1):
			dp[0][k] = 1 if k == 0 else 0

		for n in xrange(1, N+1):
			for k in xrange(1, K+1):
				dp[n][k] = (dp[n][k-1] - (dp[n-1][k-n] if k >= n else 0) + dp[n-1][k]) % M

		# print N, K, '=' * 100
		# for _ in dp:
		# 	print _

		return dp[N][K]

print Solution().kInversePairs(3, 0)
print Solution().kInversePairs(3, 1)
# print Solution().kInversePairs(3, 2)
# print Solution().kInversePairs(3, 3)