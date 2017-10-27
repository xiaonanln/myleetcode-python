class Solution(object):
	def evalRPN(self, tokens):
		"""
		:type tokens: List[str]
		:rtype: int
		"""
		stk = []
		for tok in tokens:
			# print stk, tok,
			if tok == '+':
				stk.append(stk.pop() + stk.pop())
			elif tok == '-':
				a, b= stk.pop(), stk.pop()
				stk.append(b-a)
			elif tok == '*':
				stk.append(stk.pop() * stk.pop())
			elif tok == '/':
				a, b = stk.pop(), stk.pop()
				stk.append(int(float(b) / a))
			else:
				stk.append(int(tok))

		return stk[0]

print Solution().evalRPN( ["10","6","9","3","+","-11","*","/","*","17","+","5","+"])