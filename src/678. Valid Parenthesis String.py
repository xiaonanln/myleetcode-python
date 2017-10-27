class Solution(object):
	def checkValidString(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		N = len(s)
		isValid = [[False] * (N+1) for _ in xrange(N+1)]
		for i in xrange(N+1):
			isValid[i][i] = True
			if i < N:
				isValid[i][i+1] = (s[i] == '*') # len 1 str is valid only when it's '*'

		for l in xrange(2, N+1):
			for i in xrange(N-l+1):
				j = i + l
				# print 'check', i, j, isValid[i+1][j-1]
				if s[i] == ')' or s[j-1] == '(':
					isValid[i][j] = False
					continue

				if isValid[i+1][j-1]:
					isValid[i][j] = True
					continue

				for k in xrange(i+1, j):
					if isValid[i][k] and isValid[k][j]:
						isValid[i][j] = True
						break

		# print isValid
		return isValid[0][N]

class Solution(object):
	def checkValidString(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		N = len(s)
		ns = set([0])
		for c in s:
			if c == '(':
				ns = {n+1 for n in ns}
			elif c == ')':
				ns = {n-1 for n in ns if n >= 1}
			else:
				ns = {n+z for n in ns for z in (-1, 0, 1) if n+z >= 0}

			if not ns:
				return False

		return 0 in ns


print Solution().checkValidString("")
print Solution().checkValidString("*")
print Solution().checkValidString("()")
print Solution().checkValidString("(*()")
