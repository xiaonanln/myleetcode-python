class SolutionMineFirst(object):
	def longestValidParentheses(self, s):
		def rev(s):
			return ''.join('(' if c == ')' else ')' for c in s)[::-1]

		return max(self._longestValidParentheses(s), self._longestValidParentheses(rev(s)))

	def _longestValidParentheses(self, s):
		maxlen = 0
		depth = 0
		length = 0
		for c in s:
			if c == '(':
				depth += 1
				length += 1
			elif c == ')':
				depth -= 1
				length += 1
				if depth == 0:
					maxlen = max(maxlen, length)
				elif depth < 0:
					depth = 0
					length = 0

		return maxlen

from collections import deque 
class Solution(object):
	def longestValidParentheses(self, s):
		stack = deque()
		for i, c in enumerate(s):
			if c == '(':
				stack.appendleft(i)
			else:
				if stack and s[stack[0]] == '(':
					stack.popleft()
				else:
					stack.appendleft(i)

		j = len(s)
		maxlen = 0
		while stack:
			i = stack.popleft()
			maxlen = max(maxlen, j-i-1)
			j = i

		maxlen = max(maxlen, j)
		return maxlen


print Solution().longestValidParentheses('()')