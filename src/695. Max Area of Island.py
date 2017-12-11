from collections import deque
class Solution(object):
	def maxAreaOfIsland(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		R = len(grid)
		if not R:
			return 0
		C = len(grid[0])
		q = deque()

		def dfs(r, c):
			q.append( (r, c) )
			grid[r][c] = 2
			size = 0
			while q:
				r, c = q.popleft()
				size += 1
				for nr, nc in ( (r-1, c), (r+1, c), (r, c-1), (r, c+1) ):
					if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
						grid[nr][nc] = 2
						q.append( (nr, nc) )

			return size


		maxsize = 0
		for r in xrange(R):
			for c in xrange(C):
				if grid[r][c] == 1:
					maxsize = max(maxsize, dfs(r, c))

		return maxsize

print Solution().maxAreaOfIsland(
	[[1,1,0,0,0],
	 [1,1,0,0,0],
	 [0,0,0,1,1],
	 [0,0,0,1,1]])


print Solution().maxAreaOfIsland(
	[[0,0,1,0,0,0,0,1,0,0,0,0,0],
	 [0,0,0,0,0,0,0,1,1,1,0,0,0],
	 [0,1,1,0,1,0,0,0,0,0,0,0,0],
	 [0,1,0,0,1,1,0,0,1,0,1,0,0],
	 [0,1,0,0,1,1,0,0,1,1,1,0,0],
	 [0,0,0,0,0,0,0,0,0,0,1,0,0],
	 [0,0,0,0,0,0,0,1,1,1,0,0,0],
	 [0,0,0,0,0,0,0,1,1,0,0,0,0]])

print Solution().maxAreaOfIsland(
	[[0,0,1,0,0,0,0,1,1,1,0,0,0]])
