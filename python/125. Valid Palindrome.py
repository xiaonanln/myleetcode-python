class Solution(object):
	def isPalindrome(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		L = len(s)
		i, j = 0, L - 1
		while i < j:
			while i < L and not s[i].isalnum():
				i += 1
			while j >= 0 and not s[j].isalnum():
				j -= 1

			if i >= j:
				break

			if s[i].lower() != s[j].lower():
				return False

			i+=1; j -= 1

		return True

print Solution().isPalindrome("")
print Solution().isPalindrome("A man, a plan, a canal: Panama")
print Solution().isPalindrome("race a car")