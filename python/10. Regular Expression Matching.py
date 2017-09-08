"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") = false
isMatch("aa","aa") = true
isMatch("aaa","aa") = false
isMatch("aa", "a*") = true
isMatch("aa", ".*") = true
isMatch("ab", ".*") = true
isMatch("aab", "c*a*b") = true
"""

class Solution(object):

	def interpretRegular(self, p):
		i = 0
		pl = len(p)
		interpret = []
		while i < pl:
			assert p[i] != '*'
			if i < pl-1 and p[i+1] == '*':
				interpret.append(p[i:i+2])
				i += 2
			else:
				interpret.append(p[i:i+1])
				i += 1
		return interpret

	def isMatch(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: bool
		"""
		p = self.interpretRegular(p)
		# print p

		sl = len(s)
		pl = len(p)
		M = [[False] * (pl+1) for _ in xrange(sl+1)]
		M[0][0] = True

		for i in xrange(0, sl+1):
			for j in xrange(0, pl+1):
				if i == j == 0: continue
				if i == 0:
					M[i][j] = M[i][j-1] and len(p[j-1]) == 2
				elif j == 0:
					M[i][j] = False
				else:
					pc = p[j-1]
					if pc == '.':
						M[i][j] = M[i-1][j-1]
					elif pc == '.*':
						for k in xrange(i, -1, -1): # k = i ... 0
							if M[k][j-1]:
								M[i][j] = True
								break
					elif len(pc) == 2: # 'a*', 'b*', ...
						assert pc[1] == '*'
						rc = pc[0]
						for k in xrange(i, -1, -1): # k = i ... 0
							if M[k][j-1]:
								M[i][j] = True
								break
							if s[k-1] != rc:
								break
					else:
						M[i][j] = M[i-1][j-1] and pc == s[i-1]

		return M[sl][pl]

print Solution().isMatch("aa","a")
print Solution().isMatch("aa","aa")
print Solution().isMatch("aaa","aa")
print Solution().isMatch("aa","a*")
print Solution().isMatch("aa",".*")
print Solution().isMatch("ab",".*")
print Solution().isMatch("aab", "c*a*b")
