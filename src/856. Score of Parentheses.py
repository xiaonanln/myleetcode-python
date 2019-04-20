class Solution(object):
	def scoreOfParentheses(self, S):
		"""
		:type S: str
		:rtype: int
		"""
		stack = []
		score = 0
		for c in S:
			if c == '(':
				stack.append(0)
			else:
				n = stack.pop()
				n = 1 if n == 0 else n * 2
				if stack:
					stack[-1] += n
				else:
					score += n

		return score


assert Solution().scoreOfParentheses("()") == 1
assert Solution().scoreOfParentheses("(())") == 2
assert Solution().scoreOfParentheses("()()") == 2
assert Solution().scoreOfParentheses("(()(()))") == 6
