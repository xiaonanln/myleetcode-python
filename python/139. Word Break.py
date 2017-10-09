class Solution(object):
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: bool
		"""
		if not wordDict: return s == ""
		wordDict = set(wordDict)
		MDWL = max(len(w) for w in wordDict)
		L = len(s)
		dp = [False] * (L+1)

		dp[0] = True
		for i in xrange(1, L+1):
			for j in xrange(i-1, max(0, i-MDWL) - 1, -1):
				if s[j:i] in wordDict and dp[j]:
					dp[i ] = True
					break

		return dp[len(s)]

print Solution().wordBreak("leetcode2", ["leet", "code"])