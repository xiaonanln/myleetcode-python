class Solution(object):
	def generateMatrix(self, n):
		"""
		:type n: int
		:rtype: List[List[int]]
		"""
		M = [[None] * n for _ in xrange(n)]
		dx, dy = 0, 1
		px, py = 0, -1

		nv = 1

		while nv <= n*n:
			npx, npy = px + dx, py + dy
			while 0 <= npx < n and 0 <= npy < n and M[npx][npy] is None:
				M[npx][npy] = nv
				nv += 1
				px, py = npx, npy
				npx, npy = px + dx, py + dy

			if (dx, dy) == (0, 1):
				dx, dy = 1, 0
			elif (dx, dy) == (1, 0):
				dx, dy = 0, -1
			elif (dx, dy) == (0, -1):
				dx, dy = -1, 0
			else:
				dx, dy = 0, 1

		return M

print Solution().generateMatrix(3)