class Solution(object):
	def islandPerimeter(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		R = len(grid)
		if not R:
			return 0

		C = len(grid[0])
		p = 0
		for r in xrange(R):
			for c in xrange(C):
				n = grid[r][c]
				if n:
					p += 2 + (1 if (r == 0 or not grid[r-1][c]) else -1) + (1 if (c == 0 or not grid[r][c-1]) else -1)

		return p


print Solution().islandPerimeter([[1,0]])