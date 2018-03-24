class Solution(object):
	def validPalindrome(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		L = len(s)
		i = 0
		j = L - 1
		removed = False
		while i < j:
			if s[i] == s[j]:
				i += 1
				j -= 1
				continue

			# i != j, check if we can remove i or j
			if removed:
				return False

			# print i, j, s[i], s[j], s[i:j+1]
			# now we can remove i or remove j
			s1 = s[i:j]
			if s1 == s1[::-1]: return True
			s2 = s[i+1:j+1]
			if s2 == s2[::-1]: return True
			return False

		return True

print Solution().validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga")