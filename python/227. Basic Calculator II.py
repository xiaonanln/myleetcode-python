class Solution(object):
	def calculate(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		a, aop = 0, '+'
		b, bop = 0, None
		nv = 0
		for c in s:
			if '0' <= c <= '9': # construct the value
				nv = nv * 10 + (ord(c) - ord('0'))

			elif c == ' ': continue
			elif c == '+':
				if bop is not None:
					nv = b * nv if bop == '*' else b // nv
					bop = None
				a = a + nv if aop == '+' else a - nv
				aop = '+'
				nv = 0
			elif c == '-':
				if bop is not None:
					nv = b * nv if bop == '*' else b // nv
					bop = None
				a = a + nv if aop == '+' else a - nv
				aop = '-'
				nv = 0
			elif c == '*':
				if bop is not None:
					b = b * nv if bop == '*' else b // nv
				else:
					b = nv
				bop = '*'
				nv = 0
			elif c == '/':
				if bop is not None:
					b = b * nv if bop == '*' else b // nv
				else:
					b = nv
				bop = '/'
				nv = 0

		if bop is not None:
			nv = b * nv if bop == '*' else b // nv

		return a + nv if aop == '+' else a - nv

# print Solution().calculate("3+2*2")
assert Solution().calculate("3+2*2") == 7
assert Solution().calculate(" 3/2 ") == 1
assert Solution().calculate(" 3+5 / 2 ") == 5