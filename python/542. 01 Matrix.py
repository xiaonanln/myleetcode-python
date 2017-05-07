from collections import deque
class Solution(object):
	def updateMatrix(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[List[int]]
		"""
		R = len(matrix)
		if not R: return 
		C = len(matrix[0])
		Q = deque()
		
		D = [[None] * C for _ in xrange(R)]
		for r in xrange(R):
			for c in xrange(C):
				if matrix[r][c] == 0:
					D[r][c] = 0
					Q.append((r, c))
		
		while Q:
			r, c = Q.popleft()
			d = matrix[r][c]
			for dr, dc in ( (-1, 0), (1, 0), (0, -1), (0, 1) ):
				nr, nc = r + dr, c + dc 
				if nr < 0 or nc < 0 or nr >= R or nc >= C: continue 
				# check nr, nc
				if D[nr][nc] is not None: 
					assert D[nr][nc] <= d+1
					continue 
				D[nr][nc] = d + 1
				Q.append((nr, nc))
				
		return D 
		
		
matrix = [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0, 1, 0], [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]
print Solution().updateMatrix(matrix)
print [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,2,1,1,0,1],[2,1,1,1,1,2,1,0,1,0],[3,2,2,1,0,1,0,0,1,1]]
