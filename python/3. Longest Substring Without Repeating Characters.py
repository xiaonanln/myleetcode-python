class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		cp = [-1] * 256
		st = -1
		maxlen = 0
		for i, c in enumerate(s):
			c = ord(c)
			st = max(st, cp[c] + 1)
			if i - st + 1 > maxlen:
				maxlen = i - st + 1

			cp[c] = i

		return maxlen



print Solution().lengthOfLongestSubstring("")
print Solution().lengthOfLongestSubstring("abcabcbb")
print Solution().lengthOfLongestSubstring("bbbbbb")
print Solution().lengthOfLongestSubstring("pwwkew")