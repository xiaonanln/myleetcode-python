class Solution(object):
	def isAnagram(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		cs = [0] * 26
		ct = [0] * 26

		for c in s:
			cs[ord(c) - 97] += 1
		for c in t:
			ct[ord(c) - 97] += 1

		return cs == ct