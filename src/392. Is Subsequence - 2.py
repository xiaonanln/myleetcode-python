class Solution(object):
	def isSubsequence(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		sl = len(s)
		if not sl:
			return True

		cp = 0
		for i, c in enumerate(t):
			if c == s[cp]:
				cp += 1
				if cp == sl:
					return True

		return False


s = "abc"
t = "ahbgdc"
print Solution().isSubsequence(s, t)