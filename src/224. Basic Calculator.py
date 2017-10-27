from collections import deque
class Solution(object):
	def calculate(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		stack = deque()
		ri = 0
		while True:
			tok, ri = self.readNext(s, ri)
			if tok is None:
				break

			# print 'tok', tok
			if isinstance(tok, int):
				if not stack or stack[-1] not in '+-':
					stack.append(tok)
				else:
					# calculate
					op = stack.pop()
					num0 = stack.pop()
					stack.append( num0 + tok if op == '+' else num0 - tok )
			elif tok == ')':
				num = stack.pop()
				stack.pop()

				if not stack or stack[-1] not in '+-':
					stack.append(num)
				else:
					# calculate
					op = stack.pop()
					num0 = stack.pop()
					stack.append( num0 + num if op == '+' else num0 - num )
			else:
				stack.append(tok)

			# print 'stack ==>', stack

		# assert len(stack) == 1
		return stack[0]

	def readNext(self, s, ri):
		sl = len(s)
		while ri < sl and s[ri] == ' ':
			ri += 1

		if ri >= sl:
			return None, ri

		c = s[ri]
		if c in '()+-':
			return c, ri+1

		# else it is the digit
		dstart = ri
		ri += 1
		while ri < sl and '0'<=s[ri]<='9':
			ri += 1
		num = int( s[dstart:ri] )
		return num, ri

# "1 + 1" = 2
# " 2-1 + 2 " = 3
# "(1+(4+5+2)-3)+(6+8)" = 23
# print Solution().calculate("1 + 1")
# print Solution().calculate(" 2-1 + 2 ")
print Solution().calculate("(1+(4+5+2)-3)+(6+8)")