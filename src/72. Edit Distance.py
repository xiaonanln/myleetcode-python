class Solution(object):
	def minDistance(self, word1, word2):
		"""
		:type word1: str
		:type word2: str
		:rtype: int
		"""
		L1, L2 = len(word1), len(word2)
		dp = [ [None] * (L2+1) for _ in xrange(L1+1) ]

		for i in xrange(L2+1):
			dp[0][i] = i
		for i in xrange(L1+1):
			dp[i][0] = i 

		for i in xrange(1, L1+1):
			for j in xrange(1, L2+1):
				c1 = word1[i-1]
				c2 = word2[j-1]
				if c1 == c2:
					dp[i][j] = dp[i-1][j-1]
				else:
					dp[i][j] = min(
						dp[i][j-1] + 1, 
						dp[i-1][j] + 1, 
						dp[i-1][j-1] + 1)

		return dp[L1][L2]

def check(w1, w2):
	dist = Solution().minDistance(w1, w2)
	print repr(w1), repr(w2), dist

check('', '')
check('a', 'b')