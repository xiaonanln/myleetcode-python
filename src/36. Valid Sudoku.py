class Solution(object):
	def isValidSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: bool
		"""
		if len(board) != 9: return False
		if len(board[0]) != 9: return False

		R = [0] * 9
		C = [0] * 9
		B = [0] * 9
		for r in xrange(9):
			for c in xrange(9):
				n = board[r][c]
				if n == '.': continue
				n = int(n)
				if not (1 <= n <= 9): return False
				mask = 1 << n
				if R[r] & mask:
					return False
				R[r] |= mask
				if C[c] & mask:
					return False
				C[c] |= mask
				b = (r//3)*3 + c // 3
				if B[b] & mask:
					return False
				B[b] |= mask

		return True

print Solution().isValidSudoku()