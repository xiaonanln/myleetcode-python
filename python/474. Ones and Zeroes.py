class Solution(object):
	def findMaxForm(self, strs, m, n):
		"""
		:type strs: List[str]
		:type m: int
		:type n: int
		:rtype: int
		"""
		L = len(strs)
		count1 = [0] * L
		count0 = [0] * L
		for i, s in enumerate(strs):
			count0[i] = s.count('0')
			count1[i] = s.count('1')

		memo = [
			[
				[0 if i == 0 else None] * (n+1)
				for j in xrange(m+1)
			]
			for i in xrange(len(strs)+1)]

		def find(l, i, j):
			if memo[l][i][j] is None:
				res = find(l-1, i, j)
				li, lj = i - count0[l-1], j - count1[l-1]
				if li >= 0 and lj >= 0:
					res = max(res,  1+find(l-1, li, lj) )

				memo[l][i][j] = res
			return memo[l][i][j]

		return find( L, m, n )

print Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3)
print Solution().findMaxForm(["10", "0", "1"], 1, 1)