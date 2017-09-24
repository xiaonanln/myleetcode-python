class Solution(object):
	def imageSmoother(self, M):
		"""
		:type M: List[List[int]]
		:rtype: List[List[int]]
		"""
		R = len(M)
		if not R:
			return M

		C = len(M[0])
		res = [ [0] * C for _ in xrange(R) ]
		for r in xrange(R):
			for c in xrange(C):
				n = 0
				s = 0
				for dr, dc in [ (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1) ]:
					nr, nc  = r + dr, c + dc
					if 0 <= nr < R and 0 <= nc < C:
						n += 1
						s += M[nr][nc]
				res[r][c] = s//n

		return res


print Solution().imageSmoother([[1,1,1],
 [1,0,1],
 [1,1,1]])