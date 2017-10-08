from itertools import izip

class Solution(object):
	def wordPattern(self, pattern, str):
		"""
		:type pattern: str
		:type str: str
		:rtype: bool
		"""
		patternToWord = [None] * 26
		wordToPattern = {}
		pattern = [ord(p) -  97 for p in pattern   ]

		words = str.split(' ')
		if len(pattern) != len(words):
			return False

		for c, word in izip(pattern, words):
			if patternToWord[c] is None:
				if word in wordToPattern:
					return False
				patternToWord[c] = word
				wordToPattern[word] = c

			else:
				if word not in wordToPattern or wordToPattern[word] != c:
					return False

		return True

print Solution().wordPattern("abba", "dog cat cat dog")