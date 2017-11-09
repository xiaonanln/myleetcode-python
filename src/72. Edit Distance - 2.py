
class Solution(object):
	def minDistance(self, word1, word2):
		L1 = len(word1)
		L2 = len(word2)
		dp = [[0] * (L2+1) for _ in xrange(L1+1)]
		for i in xrange(L1+1): dp[i][0] = i
		for j in xrange(L2+1): dp[0][j] = j

		for i in xrange(1, L1+1):
			for j in xrange(1, L2+1):
				if word1[i-1] == word2[j-1]:
					dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1])
				else:
					dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1]+1)

		return dp[L1][L2]

print Solution().minDistance("a", "b")