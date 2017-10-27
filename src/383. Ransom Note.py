"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
Subscribe to see which companies asked this question.
"""

from collections import Counter
class Solution(object):
	def canConstruct(self, ransomNote, magazine):
		"""
		:type ransomNote: str
		:type magazine: str
		:rtype: bool
		"""
		c1 = Counter(ransomNote)
		c2 = Counter(magazine)
		# print c1, c2, c1 - c2
		return not (c1 - c2)
print Solution().canConstruct('a', 'b')
print Solution().canConstruct('aa', 'ab')
print Solution().canConstruct('aa', 'aab')
