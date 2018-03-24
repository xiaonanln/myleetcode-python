class Solution(object):
	def candyCrush(self, board):
		"""
		:type words: List[str]
		:rtype: List[str]
		"""
		R = len(board)
		if not R: return board
		C = len(board[0])

		while True:
			zeroCols = self.markZero(board, R, C)
			# print 'zeroCols', zeroCols

			if zeroCols:
				self.dropDown(board, R, C, zeroCols)
				# print 'after dropDown:'
				# for row in board: print row
			else:
				break

		return board

	def markZero(self, board, R, C):
		zeroPoses = []
		for r in xrange(R): # check all rows
			beginCol = 0
			val = board[r][0]
			for c in xrange(1, C):
				if board[r][c] != val:
					# from beginCol to c-1 is all val
					if c - beginCol >= 3 and val != 0:
						for _c in xrange(beginCol, c):
							zeroPoses.append( (r, _c) )

					val = board[r][c]
					beginCol = c

			if C - beginCol >= 3 and val != 0:
				for _c in xrange(beginCol, C):
					zeroPoses.append((r,_c))

		for c in xrange(C): # check all cols
			beginRow = 0
			val = board[0][c]
			for r in xrange(1, R):
				if board[r][c] != val:
					if r - beginRow >= 3 and val != 0:
						for _r in xrange(beginRow, r):
							zeroPoses.append((_r, c))

					val = board[r][c]
					beginRow = r

			if R - beginRow >= 3 and val != 0:
				for _r in xrange(beginRow, R):
					zeroPoses.append((_r, c))

		for r, c in zeroPoses:
			board[r][c] = 0

		return {c for r, c in zeroPoses}

	def dropDown(self, board, R, C, cols):
		for c in cols:
			wr = R-1
			for r in xrange(R-1, -1,-1):
				if board[r][c] != 0:
					board[wr][c] = board[r][c]
					wr -= 1

			for r in xrange(wr, -1, -1):
				board[r][c] = 0

board = [[110, 5, 112, 113, 114], [210, 211, 5, 213, 214], [310, 311, 3, 313, 314], [410, 411, 412, 5, 414],
		 [5, 1, 512, 3, 3], [610, 4, 1, 613, 614], [710, 1, 2, 713, 714], [810, 1, 2, 1, 1], [1, 1, 2, 2, 2],
		 [4, 1, 4, 4, 1014]]

for row in Solution().candyCrush(board):
	print row