"""
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""

from collections import Counter
class Solution(object):
	def longestSubstring(self, s, k):
		"""
		:type s: str
		:type k: int
		:rtype: int
		"""
		C = Counter(s)
		# print s, k , C

		if not [1 for n in C.itervalues() if n < k]:
			return len(s)

		st = 0
		res = 0
		for i in xrange(0, len(s)):
			if C[s[i]] < k:
				# this char is not good
				res = max(res, self.longestSubstring(s[st:i], k))
				st = i+1

		res = max(res, self.longestSubstring(s[st:len(s)], k))

		return res

print Solution().longestSubstring('aaabb',3)
print Solution().longestSubstring('ababbc',2)
print Solution().longestSubstring("bbaaacbd",3)
