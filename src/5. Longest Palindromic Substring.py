class SolutionDP(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		if not s:
			return 0

		L = len(s)
		isPal = [ [False] * (L+1) for _ in xrange(L+1) ]
		for i in xrange(0, L):
			isPal[i][i] = True
			isPal[i][i+1] = True

		longestPal = s[0]
		for l in xrange(2, L+1):
			for i in xrange( 0, L-l+1 ):
				j = i + l
				if s[i] == s[j-1] and isPal[i+1][j-1]:
					isPal[i][j] = True
					if l > len(longestPal):
						longestPal = s[i:j]

		return longestPal

from collections import deque
class Solution(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		if not s:
			return 0

		L = len(s)
		# isPal = [[False] * (L + 1) for _ in xrange(L + 1)]
		q = deque()
		for i in xrange(0, L):
			q.append( (i, i) )
		for i in xrange(0, L):
			q.append( (i, i+1) )
			# isPal[i][i] = True
			# isPal[i][i + 1] = True

		last = None
		while q:
			i, j = q.popleft()
			# print i, j, i > 0 and j < L and s[i-1] == s[j]
			last = (i, j)
			if i > 0 and j < L and s[i-1] == s[j]:
				q.append( (i-1, j+1) )

		return s[last[0]:last[1]]


print Solution().longestPalindrome("ccc")
# print Solution().longestPalindrome("babad")