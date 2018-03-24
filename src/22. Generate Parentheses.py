class Solution(object):
	def generateParenthesis(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		all = []
		sol = ['' for _ in xrange(n * 2)]
		def bt(pos, depth):
			if pos >= n*2:
				# solution generated
				all.append( ''.join(sol) )
				return

			if (depth + 1) <= (n*2 - pos - 1):
				sol[pos] = '('
				bt(pos+1, depth+1)

			if depth > 0:
				sol[pos] = ')'
				bt(pos + 1, depth - 1)

		bt(0, 0)
		return all

print Solution().generateParenthesis(0)
print Solution().generateParenthesis(1)
print Solution().generateParenthesis(2)
print Solution().generateParenthesis(3)
