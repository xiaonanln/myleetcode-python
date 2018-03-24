
class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		stk = []
		for c in s:
			if c in '({[':
				stk.append(c)
			else:
				if not stk:
					return False

				lc = stk.pop()
				if not ((lc == '(' and c == ')') or (lc == '[' and c == ']') or (lc == '{' and c == '}')):
					# bad
					return False

		return not stk

print Solution().isValid("()[]{}")

