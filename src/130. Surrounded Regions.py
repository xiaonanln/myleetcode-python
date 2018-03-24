
from collections import deque
class Solution(object):
	def solve(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		R = len(board)
		if R <= 2: return
		C = len(board[0])
		if C <= 2: return

		self.visited = [[False]*C for _ in xrange(R)]
		for c in xrange(C):
			if not self.visited[0][c] and board[0][c] == 'O':
				self.bfs( board, 0, c, R, C)
			if not self.visited[R-1][c] and board[R-1][c] == 'O':
				self.bfs(board, R-1, c, R, C)

		for r in xrange(1, R-1):
			if not self.visited[r][0] and board[r][0] == 'O':
				self.bfs(board, r, 0, R, C)
			if not self.visited[r][C-1] and board[r][C-1] == 'O':
				self.bfs(board, r, C-1, R, C)

		for r in xrange(R):
			for c in xrange(C):
				if not self.visited[r][c] and board[r][c] == 'O':
					board[r][c] = 'X'

	def bfs(self, board, sr, sc, R, C):
		q = deque([(sr, sc)])
		self.visited[sr][sc] = True
		while q:
			r, c = q.popleft()
			for nr, nc in ( (r-1, c), (r+1,c), (r,c-1), (r,c+1) ):
				if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == 'O' and not self.visited[nr][nc]:
					self.visited[nr][nc] =True
					q.append( (nr, nc) )

board = [
	['X', 'X', 'X', 'X'],
	['X', 'O', 'O', 'X'],
	['X', 'X', 'O', 'X'],
	['X', 'O', 'X', 'X'],
]
Solution().solve(board)
for x in board: print x