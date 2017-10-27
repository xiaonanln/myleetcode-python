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
		
		D = [ [ 0 if matrix[r][c] == 0 else None for c in xrange(C)] for r in xrange(R)]
		Q = deque( [(r, c) for r in xrange(R) for c in xrange(C) if matrix[r][c] == 0] )

		while Q:
			r, c = Q.popleft()
			d = D[r][c]
			for dr, dc in ( (-1, 0), (1, 0), (0, -1), (0, 1) ):
				nr, nc = r + dr, c + dc
				if 0<=nr<R and 0<=nc<C and D[nr][nc] is None:
					D[nr][nc] = d + 1
					Q.append((nr, nc))
				
		return D 

matrix = [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0, 1, 0], [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]
for r in matrix:
	print ' '.join('%d' % d for d in r)

print '=' * 100
for r in  Solution().updateMatrix(matrix):
	print r
