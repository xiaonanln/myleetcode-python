class Solution(object):
	def numIslands(self, grid):
		"""
		:type grid: List[List[str]]
		:rtype: int
		"""
		R = len(grid)
		if R == 0: return 0
		C = len(grid[0])

		visited = [ [False] * C for _ in xrange(R)]

		def dfs(r, c):
			visited[r][c] = True
			for (dr, dc) in ( (-1, 0), (1, 0), (0, -1), (0, 1) ):
				nr, nc = (r+dr), (c+dc)
				if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == '1' and not visited[nr][nc]:
					dfs(nr, nc)

		num = 0
		for r in xrange(R):
			for c in xrange(C):
				if grid[r][c] == '1' and not visited[r][c]:
					dfs(r, c)
					num += 1

		return num


def convertToGrid(s):
	grid = [list(line.strip()) for line in s.strip().split('\n')]
	print grid
	return grid

print Solution().numIslands(convertToGrid(
	"""
	11110
	11010
	11000
	00000
	"""
))

print Solution().numIslands(convertToGrid(
	"""
	11000
	11000
	00100
	00011
	"""
))