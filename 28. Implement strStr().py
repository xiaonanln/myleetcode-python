class Solution(object):
	def strStr(self, haystack, needle):
		"""
		:type haystack: str
		:type needle: str
		:rtype: int
		"""
		
		return haystack.find(needle)


print Solution().strStr("abc", "a")


"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Subscribe to see which companies asked this question.
"""
