class Solution(object):
	def addOperators(self, num, target):
		"""
		:type num: str
		:type target: int
		:rtype: List[str]
		"""
		if not num: return []
		N = len(num)
		operators = [''] * (len(num) - 1)
		res = []

		def bt(i, a, b, sign, m, formula):
			# print 'bt', i, a, b, sign, m, formula, a + b * sign * m == target
			if i == N-1:
				# print operators
				if a + b * sign * m == target:
					res.append(formula)
				return

			if not (num[i] == '0' and (i == 0 or operators[i-1] != '')):
				operators[i] = ''
				bt(i+1, a, b*10+int(num[i+1]), sign, m, formula+num[i+1])

			for op in '+-*':
				operators[i] = op
				if op == '+':
					bt(i + 1, a + b * sign * m, int(num[i+1]), 1, 1, formula + op + num[i + 1])
				elif op == '-':
					bt(i + 1, a + b * sign * m, int(num[i+1]), -1, 1, formula + op + num[i + 1])
				elif op == '*':
					bt(i + 1, a, int(num[i+1]), sign, m*b, formula + op + num[i + 1])

		bt(0, 0, int(num[0]), 1, 1, num[0])
		return res


import cProfile
print Solution().addOperators("123", 6)
# cProfile.run("""
# print Solution().addOperators("1000000009", 9)
# """)