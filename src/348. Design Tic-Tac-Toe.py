class TicTacToe(object):
	def __init__(self, n):
		"""
		Initialize your data structure here.
		:type n: int
		"""
		self.winner = 0
		self.n = n
		self.board = [[0]*n for _ in xrange(n)]

	def move(self, row, col, player):
		"""
		Player {player} makes a move at ({row}, {col}).
		@param row The row of the board.
		@param col The column of the board.
		@param player The player, can be either 1 or 2.
		@return The current winning condition, can be either:
				0: No one wins.
				1: Player 1 wins.
				2: Player 2 wins.
		:type row: int
		:type col: int
		:type player: int
		:rtype: int
		"""
		if self.winner:
			return self.winner

		self.board[row][col] = player
		self.checkWin(row, col, player)
		return self.winner

	def checkWin(self, row, col, player):
		board = self.board
		if self._checkWin(board, row, col, player, 0, 1):
			return
		if self._checkWin(board, row, col, player, 1, 0):
			return
		if self._checkWin(board, row, col, player, 1, 1):
			return
		if self._checkWin(board, row, col, player, 1, -1):
			return

	def _checkWin(self, board, row, col, player, dr, dc):
		l1, l2 = 0, 0
		for i in xrange(1, self.n):
			r, c = row + dr*i, col + dc*i
			if 0 <= r < self.n and 0 <= c < self.n:
				p = board[r][c]
				if p != player:
					break
			else:
				break

			# p == player, good
			l1 = i

		for i in xrange(1, self.n):
			r, c = row - dr*i, col - dc*i
			if 0 <= r < self.n and 0 <= c < self.n:
				p = board[r][c]
				if p != player:
					break
			else:
				break

			# p == player, good
			l2 = i

		if l1+l2+1 >= self.n:
			self.winner = player
			return True
		else:
			return False


