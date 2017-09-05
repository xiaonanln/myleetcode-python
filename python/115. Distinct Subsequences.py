class Solution(object):
	def numDistinct(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: int
		"""
		if len(s) < len(t):
			return 0

		dp = [[0] * (len(s) + 1) for _ in xrange(len(t) + 1)]
		for i in xrange(0, len(s) + 1):
			dp[0][i] = 1

		for i in xrange(1, len(t) + 1):  # t[0:i]
			tc = t[i - 1]
			for j in xrange(1, len(s) + 1):  # s[0:j]
				sc = s[j - 1]
				if tc != sc:
					dp[i][j] = dp[i][j - 1]
				else:
					dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]

		# print dp
		return dp[len(t)][len(s)]



