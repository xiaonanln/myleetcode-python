class Solution(object):
	def reverseVowels(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		s = list(s)
		vowels = [(i, c) for i, c in enumerate(s) if c in 'aeiouAEIOU']
		LV = len(vowels)
		for vi, (i, c) in enumerate(vowels):
			i2, c2 = vowels[LV-vi-1]
			s[i] = c2

		return ''.join(s)

print Solution().reverseVowels('leetcode')