class SolutionBT(object):
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		if not digits: return []
		LETTERS = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
		N = len(digits)
		input = [''] * N
		res = []
		def bt(n):
			if n == N:
				res.append(''.join(input))
				return
			d = ord(digits[n]) - 48
			for c in LETTERS[d]:
				input[n] = c
				bt(n+1)

		bt(0)
		return res

LETTERS = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
class Solution(object):
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		if not digits: return []
		sols = ("", )
		for d in digits:
			sols = tuple(s + c for c in LETTERS[ord(d) - 48] for s in sols)
		return list(sols)



import cProfile
cProfile.run('Solution().letterCombinations("39474738294")')
