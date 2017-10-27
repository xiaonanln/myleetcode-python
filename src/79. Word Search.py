class Solution(object):
	def exist(self, board, word):
		"""
		:type board: List[List[str]]
		:type word: str
		:rtype: bool
		"""
		if not word: return True

		R = len(board)
		if not R: return False
		C = len(board[0])
		W = len(word)

		def find(r, c, idx):
			# print 'find', r, c, idx
			if board[r][c] != word[idx]: return False

			if idx == W-1: return True

			board[r][c] = ''
			for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
				nr, nc = r+dr, c+dc
				if 0<=nr<R and 0<=nc<C:
					if find(nr, nc, idx+1):
						return True

			board[r][c] = word[idx]
			return False

		for r in xrange(R):
			for c in xrange(C):
				if find(r, c, 0):
					return True
		return False




board = [
	["a"],
]

print Solution().exist(board, "a")