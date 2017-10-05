class Solution1(object):
	def solveNQueens(self, n):
		"""
		:type n: int
		:rtype: List[List[str]]
		"""
		solutions = []
		board = [['.'] * n for _ in xrange(n)]
		rows = [False] * n
		cols = [False] * n
		diag1 = [False] * (2*n-1)       # /
		diag2 = [False] * (2 * n - 1)   # \

		def nextrc(r, c):
			c += 1
			if c == n:
				r, c = r+1, 0
			return r, c

		def bt(r, c, queen):
			if queen + n - r < n:
				return

			if r == n:
				if queen == n:
					solutions.append([''.join(row) for row in board])
				return

			bt(r if c < n-1 else r+1, c+1 if c < n-1 else 0, queen) # not filling the current cell

			if not rows[r] and not cols[c] and not diag1[r+c] and not diag2[n-1-r+c]:
				board[r][c] = 'Q'
				rows[r] = cols[c] = diag1[r+c] = diag2[n-1-r+c] = True

				bt(r if c < n-1 else r+1, c+1 if c < n-1 else 0, queen+1)

				rows[r] = cols[c] = diag1[r + c] = diag2[n - 1 - r + c] = False
				board[r][c] = '.'

		bt(0, 0, 0)
		return solutions

class Solution(object):
	def solveNQueens(self, n):
		"""
		:type n: int
		:rtype: List[List[str]]
		"""
		solutions = []
		board = [['.'] * n for _ in xrange(n)]
		cols = [False] * n
		diag1 = [False] * (2*n-1)       # /
		diag2 = [False] * (2 * n - 1)   # \

		def bt(r):
			if r == n:
				solutions.append([''.join(row) for row in board])
				return

			for c in xrange(n): # check each col
				if not cols[c] and not diag1[r+c] and not diag2[n-1-r+c]:
					board[r][c] = 'Q'
					cols[c] = diag1[r+c] = diag2[n-1-r+c] = True

					bt(r+1)

					cols[c] = diag1[r + c] = diag2[n - 1 - r + c] = False
					board[r][c] = '.'

		bt(0)
		return solutions


import cProfile
cProfile.run("Solution().solveNQueens(9)")

# for board in Solution().solveNQueens(9):
# 	print '===================================='
# 	for row in board:
# 		print row